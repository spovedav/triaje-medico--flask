
// tenplate = `<tr>
//                 <th colspan="5" class="text-danger p-4 mr-4 justify-content-center bg-dange h4">No hay registro ""</th>
//                 </tr>
//                 `;
// document.getElementById("table-paciente").innerHTML = tenplate


SetFecha();

function SetFecha() {
    var f = new Date();
    if(f.getDate()<9){
        window.setFecha = f.getFullYear() + "-" + (f.getMonth() + 1) + "-0" + f.getDate();
    }else{
        window.setFecha = f.getFullYear() + "-" + (f.getMonth() + 1) + "-" + f.getDate();
    }
    var parametros = {
        "fecha": setFecha
    }
    $.ajax({
        data: parametros,
        url: '/rrellenarTabla',
        type: 'post',
        dataType: 'json',
        success: function (r) {
            var tenplate = '';
            var style = '';
            var confi = '';
            if (r.length != 0) {

                for (var valor in r) {
                    // alert( typeof(r[valor].confir));
                    if (r[valor].confir == '1') {
                        //alert('si set')
                        style = 'style="background-color: rgb(97, 255, 74); color: #000;"';
                        confi = 'checked';
                    } else {
                        style = '';
                        confi = '';
                    }
                    tenplate += `
            <tr id="cliente-${ r[valor].cod_agenda}" ${style}>
                <th scope="row"><input onchange="confi_row(this.id);" ${ confi } class="checkbox mr-2" type="checkbox" name="confir-${r[valor].cod_agenda}" id="confir-${r[valor].cod_agenda}"> ${r[valor].telf}</th>
                <th colspan="2">${ r[valor].nombre1 + ' ' + r[valor].apellido1}</th>
                <th>${ r[valor].hora}</th>
                <th>Especialidad</th>
                <th> 
                    <div class="small">
                        <form action="/cod" method="POST" class="d-inline">
                        <input type="hidden" name="cod" id="cod" value="${ r[valor].cod_agenda}">
                        <button type="button" class="ac" value="${ r[valor].cod_agenda}" id="delete" onclick="Send_Cod(this);" ><img title="Eliminar ${r[valor].nombre1}" src="../static/img/img_agendar/archivo_delete.png" alt="Eliminar"></button>
                        <button type="button" class="ac" value="${ r[valor].cod_agenda}" id="update" onclick="Send_Cod(this);"><img title="Modificar ${r[valor].nombre1}" src="../static/img/img_agendar/archivo_update.png" alt="Modificar"></button> 
                        <button type="button" class="ac" value="${ r[valor].cod_agenda}" id="admision" onclick="Send_Cod_Admision(this);"><img  title="Admisionar ${r[valor].nombre1}" src="../static/img/img_agendar/archivo_insert.png" alt="Admision"></button>
                    </div>
                </th>
            </tr>
            `
                }
            } else {
                tenplate = `<tr>
                              <th colspan="5" class="text-danger p-4 mr-4 justify-content-center bg-dange h4">No hay registro "${ setFecha }"</th>
                           </tr>
                        `;
            }


            document.getElementById("table-paciente").innerHTML = tenplate
            //alert('en');
            //location.reload();
        }
    });

}


function GetFecha() {
    //alert($("#fechaSelect").val())
    var fecha_select = $("#fechaSelect").val();
    var parametros = {
        "fecha": fecha_select
    }
    $.ajax({
        data: parametros,
        url: '/rrellenarTabla',
        type: 'post',
        dataType: 'json',
        success: function (r) {
            var tenplate = '';
            var style = '';
            var confi = '';
            if (r.length != 0) {
                for (var valor in r) {
                    // alert( typeof(r[valor].confir));
                    if (r[valor].confir == '1') {
                        //alert('si set')
                        style = 'style="background-color: rgb(97, 255, 74); color: #000;"';
                        confi = 'checked';
                    } else {
                        style = '';
                        confi = '';
                    }
                    tenplate += `
            <tr id="cliente-${ r[valor].cod_agenda}" ${ style }>
                <th scope="row"><input onchange="confi_row(this.id);" ${ confi } class="checkbox mr-2" type="checkbox" name="confir-${ r[valor].cod_agenda}" id="confir-${r[valor].cod_agenda}">${r[valor].telf}</th>
                <th colspan="2">${ r[valor].nombre1 + ' ' + r[valor].apellido1}</th>
                <th>${ r[valor].hora}</th>
                <th>Especialidad</th>
                <th> 
                    <div class="small">
                        <form action="/cod" method="POST" class="d-inline">
                        <input type="hidden" name="cod" id="cod" value="${ r[valor].cod_agenda}">
                        <button type="button" class="ac" value="${ r[valor].cod_agenda}" id="delete" onclick="Send_Cod(this);" ><img title="Eliminar ${r[valor].nombre1}" src="../static/img/img_agendar/archivo_delete.png" alt="Eliminar"></button>
                        <button type="button" class="ac" value="${ r[valor].cod_agenda}" id="update" onclick="Send_Cod(this);"><img title="Modificar ${r[valor].nombre1}" src="../static/img/img_agendar/archivo_update.png" alt="Modificar"></button> 
                        <button type="submit" class="ac" value="${ r[valor].cod_agenda}" id="admision" onclick="Send_Cod_Admision(this);"><img  title="Admisionar ${r[valor].nombre1}" src="../static/img/img_agendar/archivo_insert.png" alt="Admision"></button>
                    </div>
                </th>
            </tr>
            `
                }
            } else {
                tenplate = `<tr>
                              <th colspan="5" class="text-danger p-4 mr-4 m-auto justify-content-center bg-dange h4">No hay registro "${ fecha_select }"</th>
                           </tr>`
            }


            document.getElementById("table-paciente").innerHTML = tenplate
            //alert('en');
            //location.reload();
            //console.log(r);
        }
    });
}

function Send_Cod_Admision(e) {
    var parametros = {
        "cod": e.value
        //"bandera": e.id
    }
    $.ajax({
        data: parametros,
        url: '/cod',
        type: 'POST',
        dataType: 'json',
        success: function (r) {
            window.location.replace('/admision');   //alert(r);
        }
    });
    // 
    //alert('admin');

    if (e.id == "admision") {
        //     $.ajax({
        //         data: parametros,
        //         url: '/admision',
        //         type: 'POST',
        //         dataType: 'json',
        //         success: function (r) {
        //         }
        //     });
        // 
    }
}

function Send_Cod(e) {
    var parametros = {
        "cod": e.value,
        "bandera": e.id
    }

    var fecha_select = $("#fechaSelect").val();

    //var f = new Date();
    //var setFecha =  f.getFullYear() + "-" +  (f.getMonth() +1) + "-"+f.getDate()
    if (fecha_select == "") {
        fecha_select = setFecha;
    }


    $.ajax({
        data: parametros,
        url: '/aciones',
        type: 'POST',
        dataType: 'json',
        success: function (r) {
            if (r == 1) {
                location.reload();
            }
            var title = document.getElementById("title");
            if (e.id == "update") {
                title.innerHTML = "Modificar a " + r['nombre1'] + " " + r['apellido1'] + " " + fecha_select;
                //title.style.fontSize = 10;

                $("#cod_paciente").val(r['cod_agenda']);
                $("#nombre1").val(r['nombre1']);
                $("#apellido1").val(r['apellido1']);
                $("#telf").val(r['telf']);
                //$("#medico").append("<option value='cod'>doct</option>");
                var combo = document.getElementById("medico");
                var selected = combo.options[combo.selectedIndex].text = r['cod_doctor']+" me falto esto";
                
                $("#hora").val(r['hora']);
                $("#fecha").val(fecha_select);
                $("#observacion").val(r['observacion']);
            }
        }
    });
}

function confi_row(e) {
    var cod = e;
    //alert(cod);// - cadena.split('');
    $("#cod_row").val(cod);

    var cod_array = cod.split('-');
    var c1 = $('#confir-' + cod_array[1]).prop('checked');
    //var valor;
    var parametros = {
        "cod": cod_array[1],
        "valor": c1
    }

    $.ajax({
        data: parametros,
        url: '/confir',
        type: 'POST',
        //dataType: 'json',
        success: function (r) {
            if (r == '1') {
                window.location.reload();
            }

        }
    });
}



///////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
// SOCKETIO ****

function pruebaso() {
    alert(conn);
}


