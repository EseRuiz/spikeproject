// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
// Vuetify
import { createVuetify } from 'vuetify'
//Components
import { VDataTable } from 'vuetify/labs/VDataTable'
import { VBtn } from 'vuetify/components'
import { aliases, mdi } from 'vuetify/iconsets/mdi'

export default createVuetify(
  {
    components: {
      VDataTable,
      VBtn,
      icons: {
        defaultSet: 'mdi',
        aliases,
        sets: {
          mdi,
        }
      },
    },
  }
  // https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides

)
