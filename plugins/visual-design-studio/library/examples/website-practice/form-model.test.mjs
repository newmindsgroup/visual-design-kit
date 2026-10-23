// Version-Timestamp: 2026-09-11T20:58:31-04:00
import test from 'node:test';import assert from 'node:assert/strict';
import {next} from './form-model.mjs';
test('submission starts once',()=>{assert.equal(next('idle','submit'),'submitting');assert.equal(next('submitting','submit'),'submitting')});
test('response loss remains unknown even after retry',()=>{assert.equal(next('submitting','lost'),'unknown');assert.equal(next('unknown','submit'),'unknown');assert.equal(next('unknown','time'),'unknown')});
test('only reconciliation unlocks unknown',()=>{assert.equal(next('unknown','not-received'),'idle');assert.equal(next('unknown','received'),'received')});
test('receipt cannot be resubmitted',()=>assert.equal(next('received','submit'),'received'));
test('definite rejection allows correction',()=>{assert.equal(next('submitting','rejected'),'rejected');assert.equal(next('rejected','submit'),'submitting')});
