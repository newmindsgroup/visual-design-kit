// Visual Design Kit, MIT. Part of a Remotion example; Remotion itself is NOT MIT (see README.md "Remotion license").
// Version-Timestamp: 2026-10-23 20:12:12 UTC
//
// Plays portable Lottie files built by library/scripts/lottie_build.py (public/lottie/*.json)
// through @remotion/lottie (lottie-web underneath). Lottie colors are baked at build time:
// rebuild with `--brand` and `--mode` for another theme. The canvas behind them follows the props.
import React, {useEffect, useState} from 'react';
import {AbsoluteFill, cancelRender, continueRender, delayRender, Freeze, staticFile, useVideoConfig} from 'remotion';
import {Lottie, type LottieAnimationData} from '@remotion/lottie';
import {useTheme, type BrandProps} from '../lib/motion.ts';

export interface LottieInRemotionProps extends BrandProps {
  /** File name in public/lottie without .json. */
  animation: 'logo-reveal' | 'loader' | 'icon-morph' | 'underline-sweep';
  loop: boolean;
}

export const LottieInRemotion: React.FC<LottieInRemotionProps> = (props) => {
  const theme = useTheme(props);
  const {fps} = useVideoConfig();
  const [handle] = useState(() => delayRender(`Loading lottie/${props.animation}.json`));
  const [data, setData] = useState<LottieAnimationData | null>(null);

  useEffect(() => {
    fetch(staticFile(`lottie/${props.animation}.json`))
      .then((response) => response.json())
      .then((json: LottieAnimationData) => {
        setData(json);
        continueRender(handle);
      })
      .catch((error) => cancelRender(error));
  }, [handle, props.animation]);

  if (!data) return null;
  const width = Math.min(1200, data.w * (data.w < 300 ? 4 : 1.4));
  return (
    <AbsoluteFill style={{backgroundColor: theme.color.canvas, alignItems: 'center', justifyContent: 'center'}}>
      <div style={{width, aspectRatio: `${data.w} / ${data.h}`}}>
        {props.reducedMotion ? (
          // Reduced motion: hold the final, most meaningful frame instead of playing.
          <Freeze frame={Math.floor(((data.op - 1) / data.fr) * fps)}>
            <Lottie animationData={data} loop={false} />
          </Freeze>
        ) : (
          <Lottie animationData={data} loop={props.loop} />
        )}
      </div>
    </AbsoluteFill>
  );
};
