# Complete persona field inventory

Version-Timestamp: 2026-09-07 09:16:31 AST

Every field is required structurally. Values may be unknown or justified not applicable. Field keys remain stable across languages. See [component definitions](persona-components.json). Historical attribution is isolated in the reference audit.

| ID | Canonical field path | Group | English / original Spanish label | Type  |
| --- | --- | --- | --- | ---  |
| F001 | `id` | header | Id / No separate UI label verified | string  |
| F002 | `name` | header | Name / No separate UI label verified | string  |
| F003 | `shortName` | header | Short name / No separate UI label verified | string  |
| F004 | `image` | header | Image / No separate UI label verified | string  |
| F005 | `priority` | header | Priority / No separate UI label verified | string  |
| F006 | `demographics.age` | sidebar | Age / Edad | string  |
| F007 | `demographics.role` | sidebar | Role / Rol | string  |
| F008 | `demographics.company` | sidebar | Company / Empresa | string  |
| F009 | `demographics.industry` | sidebar | Industry / Industria | string  |
| F010 | `demographics.experience` | sidebar | Experience / Experiencia | string  |
| F011 | `demographics.education` | sidebar | Education / Educación | string  |
| F012 | `demographics.techSavviness` | sidebar | Tech Savviness / Dominio Tecnológico | string  |
| F013 | `demographics.income` | sidebar | Income / No separate UI label verified | string  |
| F014 | `demographics.location` | sidebar | Location / Ubicación | string  |
| F015 | `demographics.teamSize` | sidebar | Team Size / Tamaño del Equipo | string  |
| F016 | `demographics.reportingTo` | sidebar | Reports To / Reporta a | string  |
| F017 | `psychographics.values[]` | psychographics | Core Values / Valores Fundamentales | string item  |
| F018 | `psychographics.personality` | psychographics | Personality / Personalidad | string  |
| F019 | `psychographics.lifestyle` | psychographics | Lifestyle / Estilo de Vida | string  |
| F020 | `psychographics.attitudes` | psychographics | Attitudes / Actitudes | string  |
| F021 | `psychographics.motivations[]` | psychographics | Motivations / Motivaciones | string item  |
| F022 | `psychographics.fears[]` | psychographics | Fears / Miedos | string item  |
| F023 | `jtbd` | overview | Jobs to be Done / Trabajos por Hacer | string  |
| F024 | `goals[]` | overview | Goals / Objetivos | string item  |
| F025 | `frustrations[]` | overview | Frustrations / Frustraciones | string item  |
| F026 | `painPoints[].pain` | overview | Detailed Pain Points / Puntos de Dolor Detallados | string item  |
| F027 | `painPoints[].urgency` | overview | urgency / urgencia | string item  |
| F028 | `painPoints[].impact` | overview | impact / impacto | string item  |
| F029 | `painPoints[].currentWorkaround` | overview | Current / Actual | string item  |
| F030 | `painPoints[].desiredSolution` | overview | Desired / Deseado | string item  |
| F031 | `behaviors[]` | overview | Key Behaviors / Comportamientos Clave | string item  |
| F032 | `quote` | header | Quote / No separate UI label verified | string  |
| F033 | `scenarios[].name` | scenarios | Name / No separate UI label verified | string item  |
| F034 | `scenarios[].description` | scenarios | Description / No separate UI label verified | string item  |
| F035 | `scenarios[].trigger` | scenarios | Trigger / Disparador | string item  |
| F036 | `scenarios[].outcome` | scenarios | Outcome / Resultado | string item  |
| F037 | `influences.sources[]` | journey | Information Sources / Fuentes de Información | string item  |
| F038 | `influences.decisionFactors[]` | journey | Decision Factors / Factores de Decisión | string item  |
| F039 | `influences.influencers[]` | journey | Influencers / Influenciadores | string item  |
| F040 | `influences.peerInfluence` | journey | Peer Influence / Influencia de Pares | string  |
| F041 | `buyingJourney.awareness.triggers[]` | journey | Triggers / Disparadores | string item  |
| F042 | `buyingJourney.awareness.questions[]` | journey | Questions They Ask / Preguntas que Hacen | string item  |
| F043 | `buyingJourney.consideration.evaluationCriteria[]` | journey | Evaluation Criteria / Criterios de Evaluación | string item  |
| F044 | `buyingJourney.consideration.objections[]` | journey | Objections / No separate UI label verified | string item  |
| F045 | `buyingJourney.decision.finalTriggers[]` | journey | Final triggers / No separate UI label verified | string item  |
| F046 | `buyingJourney.decision.barriers[]` | journey | Barriers / Barreras | string item  |
| F047 | `contentPreferences.formats[]` | content | Preferred Formats / Formatos Preferidos | string item  |
| F048 | `contentPreferences.channels[]` | content | Preferred Channels / Canales Preferidos | string item  |
| F049 | `contentPreferences.tone` | content | Tone & Style / Tono y Estilo | string  |
| F050 | `contentPreferences.topics[]` | content | Interested In / Interesado En | string item  |
| F051 | `communicationStyle.persuasionStyle` | content | Persuasion Style / Estilo de Persuasión | string  |
| F052 | `communicationStyle.proofPoints[]` | content | Proof Points That Work / Puntos de Prueba que Funcionan | string item  |
| F053 | `communicationStyle.keyPhrases[]` | content | Key Phrases That Resonate / Frases Clave que Resuenan | string item  |
| F054 | `successMetrics.winDefinition` | scenarios | Win Definition / Definición de Éxito | string  |
| F055 | `successMetrics.personalSuccess[]` | scenarios | Personal Success / Éxito Personal | string item  |
| F056 | `successMetrics.professionalSuccess[]` | scenarios | Professional Success / Éxito Profesional | string item  |
| F057 | `successMetrics.kpis[]` | scenarios | Kpis / No separate UI label verified | string item  |
| F058 | `objections[].objection` | objections | Objections & Responses / Objeciones y Respuestas | string item  |
| F059 | `objections[].response` | objections | Recommended Response / Respuesta Recomendada | string item  |
| F060 | `objections[].proofNeeded` | objections | Proof Needed / Prueba Necesaria | string item  |
| F061 | `technologyUsage.devices[]` | sidebar | Devices / Dispositivos | string item  |
| F062 | `technologyUsage.mobileVsDesktop` | sidebar | Device Preference / Preferencia de Dispositivo | string  |
| F063 | `technologyUsage.preferredApps[]` | sidebar | Preferred apps / No separate UI label verified | string item  |
| F064 | `technologyUsage.digitalBehavior` | sidebar | Digital behavior / No separate UI label verified | string  |
| F065 | `decisionCriteria.mustHaves[]` | journey | Must Haves / Imprescindibles | string item  |
| F066 | `decisionCriteria.niceToHaves[]` | journey | Nice to Haves / Deseables | string item  |
| F067 | `decisionCriteria.dealBreakers[]` | journey | Deal Breakers / Factores de Rechazo | string item  |
| F068 | `competitiveContext.currentSolutions[]` | objections | Current Solutions / Soluciones Actuales | string item  |
| F069 | `competitiveContext.switchingBarriers[]` | objections | Switching Barriers / Barreras de Cambio | string item  |
| F070 | `competitiveContext.competitorPerceptions[].competitor` | objections | Competitor / No separate UI label verified | string item  |
| F071 | `competitiveContext.competitorPerceptions[].perception` | objections | Perception / No separate UI label verified | string item  |
| F072 | `emotionalJourney.beforeEngagement.mindset` | psychographics | Mindset / No separate UI label verified | string  |
| F073 | `emotionalJourney.beforeEngagement.emotions[]` | psychographics | Emotions / No separate UI label verified | string item  |
| F074 | `emotionalJourney.beforeEngagement.needs[]` | psychographics | Needs / No separate UI label verified | string item  |
| F075 | `emotionalJourney.duringConsideration.mindset` | psychographics | Mindset / No separate UI label verified | string  |
| F076 | `emotionalJourney.duringConsideration.emotions[]` | psychographics | Emotions / No separate UI label verified | string item  |
| F077 | `emotionalJourney.duringConsideration.needs[]` | psychographics | Needs / No separate UI label verified | string item  |
| F078 | `emotionalJourney.atDecision.mindset` | psychographics | Mindset / No separate UI label verified | string  |
| F079 | `emotionalJourney.atDecision.emotions[]` | psychographics | Emotions / No separate UI label verified | string item  |
| F080 | `emotionalJourney.atDecision.needs[]` | psychographics | Needs / No separate UI label verified | string item  |
| F081 | `emotionalJourney.afterPurchase.mindset` | psychographics | Mindset / No separate UI label verified | string  |
| F082 | `emotionalJourney.afterPurchase.emotions[]` | psychographics | Emotions / No separate UI label verified | string item  |
| F083 | `emotionalJourney.afterPurchase.needs[]` | psychographics | Needs / No separate UI label verified | string item  |
| F084 | `dayInTheLife.morningRoutine` | psychographics | Morning / Mañana | string  |
| F085 | `dayInTheLife.workActivities[]` | psychographics | Work Activities / Actividades de Trabajo | string item  |
| F086 | `dayInTheLife.challenges[]` | psychographics | Daily Challenges / Desafíos Diarios | string item  |
| F087 | `dayInTheLife.endOfDay` | psychographics | End of Day / Fin del Día | string  |
| F088 | `dayInTheLife.interactionPoints[]` | psychographics | Interaction points / No separate UI label verified | string item  |
| F089 | `contentMapping.awareness[]` | content | Awareness / Conocimiento | string item  |
| F090 | `contentMapping.consideration[]` | content | Consideration / Consideración | string item  |
| F091 | `contentMapping.decision[]` | content | Decision / Decisión | string item  |
| F092 | `contentMapping.retention[]` | content | Retention / Retención | string item  |
| F093 | `influences.brands[]` | journey | Trusted Brands / Marcas de Confianza | string item  |
| F094 | `buyingJourney.awareness.channels[]` | journey | Preferred Channels / Canales Preferidos | string item  |
| F095 | `buyingJourney.awareness.contentNeeds[]` | journey | Content needs / No separate UI label verified | string item  |
| F096 | `buyingJourney.consideration.criteria[]` | journey | Criteria / No separate UI label verified | string item  |
| F097 | `buyingJourney.consideration.comparisons[]` | journey | Compares Against / Compara Con | string item  |
| F098 | `buyingJourney.consideration.contentNeeds[]` | journey | Content needs / No separate UI label verified | string item  |
| F099 | `buyingJourney.decision.factors[]` | journey | Decision Factors / Factores de Decisión | string item  |
| F100 | `buyingJourney.decision.stakeholders[]` | journey | Stakeholders / Partes Interesadas | string item  |
| F101 | `buyingJourney.decision.timeline` | journey | Timeline / Cronograma | string  |
| F102 | `buyingJourney.decision.contentNeeds[]` | journey | Content needs / No separate UI label verified | string item  |
| F103 | `contentPreferences.readingLevel` | content | Reading Level / Nivel de Lectura | string  |
| F104 | `contentPreferences.length` | content | Preferred Length / Longitud Preferida | string  |
| F105 | `contentPreferences.frequency` | content | Frequency / Frecuencia | string  |
| F106 | `contentPreferences.avoidTopics[]` | content | Avoid / Evitar | string item  |
| F107 | `communicationStyle.languageLevel` | content | Language Level / Nivel de Lenguaje | string  |
| F108 | `communicationStyle.formality` | content | Formality / Formalidad | string  |
| F109 | `communicationStyle.avoidPhrases[]` | content | Phrases to AVOID / Frases a EVITAR | string item  |
| F110 | `objections[].category` | objections | Category / No separate UI label verified | string item  |
| F111 | `technologyUsage.platforms[]` | sidebar | Platforms / No separate UI label verified | string item  |
| F112 | `technologyUsage.socialMedia[]` | sidebar | Social Media / Redes Sociales | string item  |
| F113 | `technologyUsage.adoptionStyle` | sidebar | Adoption Style / Estilo de Adopción | string  |
| F114 | `decisionCriteria.priorityOrder[]` | journey | Priority order / No separate UI label verified | string item  |
| F115 | `competitiveContext.alternatives[]` | objections | Alternatives / No separate UI label verified | string item  |
| F116 | `emotionalJourney.duringConsideration.concerns[]` | psychographics | Concerns / No separate UI label verified | string item  |
| F117 | `emotionalJourney.afterPurchase.desiredEmotions[]` | psychographics | Desired emotions / No separate UI label verified | string item  |
| F118 | `emotionalJourney.afterPurchase.successIndicators[]` | psychographics | Success indicators / No separate UI label verified | string item  |

Fields present in source data but omitted by the visible renderer remain required in the canonical record. Their containing group supplies presentation; do not invent a source label or imply that hidden data appeared visually. Lists repeat without a fixed count; unknown lists carry an explicit status rather than fabricated entries. No field has an automatic factual default.
