// Visual Design Kit, MIT. Uses Remotion, which is NOT MIT: source-available under the Remotion License.
// Read README.md "Remotion license" before rendering for a company of 4 or more people.
// Version-Timestamp: 2026-10-23 20:12:12 UTC
import {Config} from '@remotion/cli/config';

Config.setVideoImageFormat('jpeg');
Config.setJpegQuality(92);
Config.setOverwriteOutput(true);
// H.264 in a yuv420p MP4 plays everywhere; the README lists per-platform overrides.
Config.setCodec('h264');
Config.setPixelFormat('yuv420p');
