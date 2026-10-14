// Version-Timestamp: 2026-10-14 11:06:44 AST
// Loaded only after an explicit experimental preview starts.
export async function createScene(canvas) {
 const THREE=await import('three');
 let renderer;
 try { renderer=new THREE.WebGLRenderer({canvas,alpha:true,antialias:true}); }
 catch(error){throw new Error('WebGL is unavailable. The static study remains visible.',{cause:error});}
 const scene=new THREE.Scene(),camera=new THREE.PerspectiveCamera(40,1,.1,100);
 camera.position.z=5;
 const geometry=new THREE.TorusKnotGeometry(.7,.18,100,12);
 const material=new THREE.MeshNormalMaterial(); const object=new THREE.Mesh(geometry,material);scene.add(object);
 let disposed=false,frame=0,playing=false,last=0;
 const render=(now)=>{frame=0;if(disposed||!playing)return;const delta=Math.min((now-last)/1000,.05);last=now;object.rotation.y+=delta*.35;object.rotation.x+=delta*.12;renderer.render(scene,camera);frame=requestAnimationFrame(render);};
 function stop(){playing=false;cancelAnimationFrame(frame);frame=0;}
 function resize(){if(disposed)return;const b=canvas.getBoundingClientRect();renderer.setPixelRatio(Math.min(devicePixelRatio||1,2));renderer.setSize(Math.max(b.width,1),Math.max(b.height,1),false);camera.aspect=Math.max(b.width,1)/Math.max(b.height,1);camera.updateProjectionMatrix();renderer.render(scene,camera);}
 resize();
 return {start(){if(disposed||playing)return;playing=true;last=performance.now();frame=requestAnimationFrame(render);},stop,resize,dispose(){if(disposed)return;disposed=true;stop();geometry.dispose();material.dispose();if(!renderer.getContext().isContextLost())renderer.forceContextLoss();renderer.dispose();}};
}
