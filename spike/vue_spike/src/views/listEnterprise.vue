<template > 
    <v-app>
      <v-form>
        <v-container>
            <v-main>
                <v-data-table
                :headers="headers"
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
                            <v-dialog v-model="dialog" max-width="600px" transition="dialog-top-transition">
                                <template v-slot:activator="{props}">
                                    <v-btn density="compact" icon="mdi-plus" color="primary" v-bind="props"
                                        variant="flat"
                                    ></v-btn>
                                </template>
                                <v-card>
                                    <v-card-title>
                                        <span class="text-h5">{{formTitle}}</span>
                                    </v-card-title>
                                    <v-card-text>
                                        <v-container>
                                            <v-row>
                                                <v-col cols="12" sm="6" md="4">
                                                    <v-text-field label="Nombre*" required v-model.trim="form.name"></v-text-field>
                                                </v-col>
                                                <v-col cols="12" sm="6" md="4">
                                                    <v-text-field label="Email*" required v-model.trim="form.email"></v-text-field>
                                                </v-col>
                                                <v-col cols="12" sm="6" md="4">
                                                    <v-text-field label="Telefono" v-model.trim="form.phone"></v-text-field>
                                                </v-col>
                                            </v-row>
                                        </v-container>
                                        <small> (*) Indica los componentes requeridos</small>
                                    </v-card-text>
                                    <v-card-actions>
                                        <v-spacer></v-spacer>
                                        <v-btn color="blue ligthen-2" outlined @click="save" >
                                            <v-icon icon="fa:fas fa-edit"></v-icon>aceptar</v-btn>
                                        <v-btn color="red accent-4" outlined @click="dialogEditClose">
                                            <v-icon variant="danger"></v-icon>Cancelar</v-btn>
                                    </v-card-actions>
                                </v-card>
                            </v-dialog>
                            <v-dialog v-model="dialogDelete" max-width="500px">
                                <v-card>
                                    <v-card-title class="text-h5">Confirma eliminacion</v-card-title>
                                    <v-card-actions>
                                        <v-spacer></v-spacer>
                                        <v-btn color="danger" text @click="dialogDelClose">Cancelar</v-btn>
                                        <v-btn color="blue darken-1" text @click="confBorrarItem">Ok</v-btn>
                                    </v-card-actions>
                                </v-card>
                            </v-dialog>
                        </v-toolbar>
                    </template>
                    <template v-slot:[`item.accion`]="{item}">
                        <div>
                            <v-btn @click=" editItem(item)" icon="mdi-pencil">
                            </v-btn>
                            <v-btn @click=" borrarItem(item)" icon="mdi-delete-outline">
                            </v-btn>
                        </div>
                    </template>
                </v-data-table>
            </v-main>
        </v-container>
      </v-form>
    </v-app>
</template>  
  <script>
  import swal from "sweetalert"
  import axios from "axios" 
  export default { 
    data() { 
      return { 
        form:{
            name:'',
            email:'',
            phone:'',
        },
        headers:[
          {title:"Nombre", key:"name"},
          {title:"Email",key:"email"},
          {title:"Telefono",key:"phone"},
          {title:"Activo",key:"active"},
          {title:"Accion",key:"accion"}
        ],
        Empresa: [], 
        editIndex:-1,
        dialog:false,
        dialogDelete:false,
      }; 
    }, 
    computed:{
        formTitle(){
            console.log("ind",this.editIndex)
            return this.editIndex===-1? "Nuevo Cliente" : "Editar Cliente"
        }
    },
    methods: { 
      //Llamar datos de la Api y guardarlos en Empresa  GET
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
      },
    //POST
      onSubmit2(){
        const path = `http://localhost:8000/api/empresa/`; 
        axios.post(path,this.form).then((response)=>{
            this.form.name=response.data.name
            this.form.email=response.data.email
            this.form.phone=response.data.phone
            swal("Empresa creada exitosamente",{buttons:false,timer:500})
            this.dialog=false
            setTimeout(()=>(300));
            window.location.reload()
        })
        .catch((error)=>{
            swal("Cliente no se ha creado","","failure")
            console.log(error)
        })
      },
    //Guardar cambios edicion PATCH,RETRIEVE
      onSubmit(){
        const path=`http://localhost:8000/api/empresa/${this.id}/`;
        axios.put(path,this.form).then((response)=>{
            this.form.name=response.data.name
            this.form.email=response.data.email
            this.form.phone=response.data.phone
            swal("Cliente editado exitosamente",{buttons:false,timer:800})
            this.dialog = false
            setTimeout(()=>(300));
            window.location.reload()
        })
        .catch((error)=>{
            swal("La empresa no se ha creado", "", "failure")
            console.log(error)
        })
      },
      editItem(empresaId){
          this.id=empresaId.raw.id
          this.editIndex=this.id
          this.editedIndex=this.Empresa.valueOf(empresaId.raw)
          this.form=Object.assign({},empresaId.raw)
          console.log("form",this.form)
          this.dialog=true
      },
      dialogEditClose(){
        this.id=-1
        this.editIndex=-1
        this.form.nombre=''
        this.form.email=''
        this.form.telefono=''
        this.dialog=false
      },
      borrarItem(empresaId){
          this.id=empresaId.value
          this.dialogDelete=true
      },
      confBorrarItem(){
        console.log("id a borrar",this.id)
        const path=`http://localhost:8000/api/empresa/${this.id}/`
        axios.delete(path).then((response)=>{
            swal("Equipo eliminado correctamente", "", "success")
            this.dialogDelete=false
            return response
        })
        .catch((error)=>{
            console.log(error)
            swal("No fue posible eliminar la empresa","","error")
        })
      },
      dialogDelClose(){
        this.id=-1
        this.editIndex=-1
        console.log("ind",this.editIndex)
        this.dialogDelete=false
      },
    //guardar
    save(){
        if(this.editIndex>-1){
            this.onSubmit()
        }
        else{
            this.onSubmit2()
        }
      },
    }, 

    created() { 
      this.getEmpresa() 
    }, 
  } 
</script> 
  <style lang="css" scoped> 
</style>