// Version-Timestamp: 2026-10-14 11:06:44 AST
import test from 'node:test';
import assert from 'node:assert/strict';
import { clamp, progress, canAnimate, createScope, frameDelta } from '../src/lib/runtime.mjs';
test('control values reject nonfinite input and clamp to limits',()=>{
 assert.equal(clamp(NaN,0,1),0);assert.equal(clamp(Infinity,0,1),0);
 assert.equal(clamp(-10,0,1),0);assert.equal(clamp(10,0,1),1);assert.equal(clamp(.4,0,1),.4);
});
test('scroll progress handles no scroll and stays in range',()=>{
 assert.equal(progress(100,100,100),0);assert.equal(progress(-10,200,100),0);
 assert.equal(progress(50,200,100),.5);assert.equal(progress(300,200,100),1);
});
test('motion requires explicit playing state and visible, active context',()=>{
 assert.equal(canAnimate({playing:true,visible:true}),true);
 for (const state of [{playing:false,visible:true},{playing:true,visible:false},{playing:true,visible:true,reduced:true},{playing:true,visible:true,hidden:true}]) assert.equal(canAnimate(state),false);
});
test('scope tears down once, in reverse order, including late registrations',()=>{
 const calls=[]; const scope=createScope();scope.add(()=>calls.push(1));scope.add(()=>calls.push(2));
 scope.dispose();scope.dispose();scope.add(()=>calls.push(3));assert.deepEqual(calls,[2,1,3]);assert.equal(scope.disposed,true);
});
test('a failed cleanup cannot prevent remaining cleanups',()=>{
 const calls=[];const scope=createScope();scope.add(()=>calls.push('safe'));scope.add(()=>{throw Error('cleanup')});
 assert.equal(scope.dispose().length,1);assert.deepEqual(calls,['safe']);
});
test('listeners attached through a scope stop receiving events after teardown',()=>{
 const target=new EventTarget();let count=0;const scope=createScope();scope.listen(target,'change',()=>count++);
 target.dispatchEvent(new Event('change'));scope.dispose();target.dispatchEvent(new Event('change'));assert.equal(count,1);
});

test("frame delta normalizes refresh rates and caps stalled frames",()=>{assert.equal(frameDelta(1000,990),.01);assert.equal(frameDelta(1000,0),.05);assert.equal(frameDelta(10,20),0);assert.equal(frameDelta(NaN,10),0);});
