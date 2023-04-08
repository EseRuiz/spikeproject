<template  > 
    <v-form>
        <v-container>
            <v-data-table
            :headers="fields"
            :items="Empresa"
            class="elevation-5"
            >
            <template v-slot:top>
                <v-toolbar>
                    <v-toolbar-title>Empresas</v-toolbar-title>
                </v-toolbar>
            </template>
            </v-data-table>
        </v-container>
    </v-form>
</template>  
<script>
import axios from "axios" 
export default { 
  data() { 
    return { 
      fields: [ 
        { key: "name", label: "Nombre" }, 
        { key: "email", label: "Email" }, 
        { key: "phone", label: "Telefono" }, 
        { key: "active", label: "active" }, 
      ], 
      Empresa: [], 
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