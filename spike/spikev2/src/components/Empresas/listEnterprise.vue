<template lang="html" > 
    <v-form>
        <v-container>
            <v-main>
                <v-data-table
                :headers="fields"
                :items="Empresa"
                class="elevation-5"
            >
                    <template v-slot:top>
                        <v-toolbar>
                            <v-toolbar-title>Empresas</v-toolbar-title>
                            <v-divider
                                class="mx-8"
                                inset
                                vertical 
                            ></v-divider>
                            <v-spacer></v-spacer>
                            <v-dialog v-model="dialog" max-width="500px" transition="dialog-top-transition">
                                <template v-slot:activator="{on, attrs}">
                                    <v-btn color="primary" v-bind="attrs"
                                        v-on="on"
                                    ><v-icon>mdi-plus box multiple</v-icon></v-btn>
                                </template>
                            </v-dialog>
                        </v-toolbar>
                    </template>
                </v-data-table>
            </v-main>
        </v-container>
    </v-form>
</template>  

<script>
import axios from "axios" 
export default { 
  data() { 
    return { 
      fields: [ 
        { text: "Nombre", value: "name" }, 
        { text: "Email",   value: "email" }, 
        { text: "Telefono",  value: "phone" }, 
        { text: "Activo", value: "active" }, 
      ],
      Empresa: [], 
      dialog:false,
    }; 
  }, 
  methods: { 
    getEmpresa() { 
      const path = 'http://localhost:8000/api/empresa/'; 
      axios 
        .get(path) 
        .then((response) => { 
          this.Empresa = response.data; 
        }) 
        .catch((error) => { 
          console.log(error); 
        }); 
    } 
  }, 
  created() { 
    this.getEmpresa() 
  }, 
} 
</script> 
<style lang="css" scoped> 
</style>