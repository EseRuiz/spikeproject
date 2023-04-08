import Vue from 'vue'
import App from './App.vue'
import router from './router'

import VueMdijs from 'vue-mdijs' 
import { mdiMagnify } from '@mdi/js' 
import { mdiPlusBoxMultiple } from '@mdi/js';

import vuetify from './plugins/vuetify' 

Vue.config.productionTip = false
VueMdijs.add({ mdiMagnify }) 
VueMdijs.add({ mdiPlusBoxMultiple }) 
Vue.use(VueMdijs)

new Vue({
  router,
  vuetify,
  render: function (h) { return h(App) }
}).$mount('#app')
