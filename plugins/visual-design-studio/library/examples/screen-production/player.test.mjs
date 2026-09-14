// Version-Timestamp: 2026-09-11 20:20:00 AST
import test from 'node:test';
import assert from 'node:assert/strict';
import {transition} from './player-model.mjs';
const initial={index:0,playing:false};
test('paused ticks preserve selection',()=>assert.deepEqual(transition(initial,'tick'),initial));
test('play advances and wraps',()=>{let s=transition(initial,'play');for(let i=0;i<3;i++)s=transition(s,'tick');assert.equal(s.index,0);assert.equal(s.playing,true)});
test('hidden and reduced motion stop playback',()=>{for(const event of ['hidden','reduced'])assert.equal(transition({index:1,playing:true},event).playing,false)});
test('manual selection pauses playback',()=>assert.deepEqual(transition({index:1,playing:true},'next'),{index:2,playing:false}));
test('unknown events cannot mutate state',()=>assert.deepEqual(transition(initial,'sensor-unverified'),initial));
