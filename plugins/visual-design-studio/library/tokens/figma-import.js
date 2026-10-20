// Visual Design Kit: import figma-variables.json into the open Figma design file.
// Version-Timestamp: 2026-10-20 02:04:10 UTC
//
// Run through the Figma MCP `use_figma` tool (load the figma-use skill first). Do not paste this file alone:
// `python3 library/scripts/tokens.py figma-script` prints `const DATA = <figma-variables.json>;` followed by
// this file, which is the complete script. Plain JavaScript with top-level await; the tool supplies `figma`.
//
// Idempotent: collections, modes and variables are matched by name and updated in place, so re-running after
// a token change updates values without breaking existing bindings. Two passes: create every variable, then
// set values, so aliases can point at variables created later in the same run.

const report = { collections: [], created: 0, updated: 0, skipped: [] };
const existingCollections = await figma.variables.getLocalVariableCollectionsAsync();
const existingVariables = await figma.variables.getLocalVariablesAsync();
const collectionByName = {};
const modeIdsByCollection = {};
const variableByKey = {};
const keyOf = (collectionName, variableName) => collectionName + "::" + variableName;

for (const spec of DATA.collections) {
  let collection = existingCollections.find((c) => c.name === spec.name);
  if (!collection) collection = figma.variables.createVariableCollection(spec.name);
  const modeIds = {};
  spec.modes.forEach((modeName, index) => {
    let mode = collection.modes.find((m) => m.name === modeName);
    if (!mode && index === 0 && collection.modes.length === 1 && !spec.modes.includes(collection.modes[0].name)) {
      collection.renameMode(collection.modes[0].modeId, modeName); // a new collection starts with "Mode 1"
      mode = collection.modes[0];
    }
    modeIds[modeName] = mode ? mode.modeId : collection.addMode(modeName);
  });
  collectionByName[spec.name] = collection;
  modeIdsByCollection[spec.name] = modeIds;
  report.collections.push({ name: spec.name, id: collection.id, modes: spec.modes });
}

for (const spec of DATA.collections) {
  const collection = collectionByName[spec.name];
  for (const item of spec.variables) {
    let variable = existingVariables.find((v) => v.variableCollectionId === collection.id && v.name === item.name);
    if (variable && variable.resolvedType !== item.type) {
      report.skipped.push(item.name + ": exists with type " + variable.resolvedType + ", expected " + item.type);
      continue;
    }
    try {
      if (!variable) {
        variable = figma.variables.createVariable(item.name, collection, item.type);
        report.created += 1;
      } else {
        report.updated += 1;
      }
    } catch (error) {
      report.skipped.push(item.name + ": " + String(error)); // e.g. TIMING/EASING in files without motion variables
      continue;
    }
    if (item.scopes) variable.scopes = item.scopes;
    if (item.description) variable.description = item.description;
    if (item.hiddenFromPublishing) variable.hiddenFromPublishing = true;
    for (const [platform, syntax] of Object.entries(item.codeSyntax || {})) {
      variable.setVariableCodeSyntax(platform, syntax);
    }
    variableByKey[keyOf(spec.name, item.name)] = variable;
  }
}

for (const spec of DATA.collections) {
  for (const item of spec.variables) {
    const variable = variableByKey[keyOf(spec.name, item.name)];
    if (!variable) continue;
    for (const [modeName, value] of Object.entries(item.valuesByMode)) {
      const modeId = modeIdsByCollection[spec.name][modeName];
      if (value && value.alias) {
        const target = variableByKey[keyOf(value.alias.collection || spec.name, value.alias.name)];
        if (!target) {
          report.skipped.push(item.name + " (" + modeName + "): alias target " + value.alias.name + " missing");
          continue;
        }
        variable.setValueForMode(modeId, figma.variables.createVariableAlias(target));
      } else {
        if (item.type === "STRING" && item.name.startsWith("font/")) {
          try {
            await figma.loadFontAsync({ family: value, style: "Regular" }); // bound text nodes need the font loaded
          } catch (error) {
            report.skipped.push(item.name + ": font " + value + " not available in this file (value still set)");
          }
        }
        variable.setValueForMode(modeId, value);
      }
    }
  }
}

return report;
