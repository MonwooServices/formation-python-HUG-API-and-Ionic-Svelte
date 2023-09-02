
import { CapacitorConfig } from '@capacitor/cli';

//const appId = 'ionic-sveltekit-ssr-demo.ionic.io';
//const appName = 'ionic-sveltekit-ssr-demo';
const server = process.argv.includes('-hmr') ? {
  'url': 'http://192.168.1.10:5173',   // always have http:// in url
  'cleartext': true
} : {};
const webDir = 'build';

const config: CapacitorConfig = {
  appId: 'com.buddy.app',
  appName: 'Buddy_app',
  webDir,
  server
};

if (process.argv.includes('-hmr')) console.log('WARNING: running capacitor with livereload config', config);

export default config;
  