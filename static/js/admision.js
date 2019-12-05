const form = document.getElementById('formAdmision');
var f = new Date();

if (f.getDate() < 9) {
    window.setFecha = f.getFullYear() + "-" + (f.getMonth() + 1) + "-0" + f.getDate();
} else {
    window.setFecha = f.getFullYear() + "-" + (f.getMonth() + 1) + "-" + f.getDate();
}
form.addEventListener('submit', function (e) {
    e.preventDefault();
    var cedula, cod_agenda, nombre1, nombre2, apellido1, apellido2;
    var sexo, e_civil, domicilio, telef_domicilio, celular, correo;
    // nombre1 =
    // nombre2 = 
    // apellido1 = 
    // apellido2 = 
    // sexo = 
    // e_civil = 
    // domicilio = 
    // telef_domicilio = 
    // celular = 
    // correo =
    cod_agenda = document.getElementById('cod_paciente').value;
    if (cod_agenda == '' || cod_agenda <= 0) {
        cod_agenda = 0;
    } else {
        cod_agenda = cod_agenda;
    }

    cedula = document.getElementById('cedula').value;
    fecha_nacimiento = document.getElementById('fecha_nacimiento').value;
    nombre1 = document.getElementById('nombre1').value;
    nombre2 = document.getElementById('nombre2').value;
    apellido1 = document.getElementById('apellido1').value;
    apellido2 = document.getElementById('apellido2').value;

    sexo = document.getElementById('sexo').value;
    e_civil = document.getElementById('e_civil').value;
    domicilio = document.getElementById('domicilio').value;
    telef_domicilio = document.getElementById('telef_domicilio').value;
    celular = document.getElementById('celular').value;
    correo = document.getElementById('correo').value;

    var parametros = {
        "cedula": cedula,
        "fecha_nacimiento": fecha_nacimiento,
        "nombre1": nombre1,
        "nombre2": nombre2,
        "apellido1": apellido1,
        "apellido2": apellido2,
        "sexo": sexo,
        "e_civil": e_civil,
        "domicilio": domicilio,
        "telef_domicilio": telef_domicilio,
        "celular": celular,
        "correo": correo,
        "fecha_ingreso": setFecha,
        "cod_agenda": cod_agenda,
        "bandera": 'insert'
    }

    $.ajax({
        data: parametros,
        url: 'crud_admision',
        type: 'POST',
        dataType: 'JSON',
        success: function (r) {
            apellido1.value = '';
            if (r>0) {
                alert('se envio la informacion de '+nombre1+' '+nombre2+' '+apellido1)
                form.onreset();
                
            }else{
                alert('Error');
            }
        }
    });
});




function buscar_paciente(e) {
    var parametros = {
        "buscar": e
    }
    $.ajax({
        data: parametros,
        url: 'buscar_paciente_admin',
        type: 'POST',
        dataType: 'json',
        success: function (r) {
            //`cod_historial`, `nombre1`, `nombre2`, `apellido1`, `apellido2`, `cedula`, `fecha_nacimiento`, `sexo`, `estado_civil`, 
            //`domicilio`, `telef_domicilio`, `celular`, `correo`
            //alert(r['nombre1']);
            //alert('si');
            if (r.length != 0) {
                nombre1.value = r[0].nombre1;
                nombre2.value = r[0].nombre2;
                apellido1.value = r[0].apellido1;
                apellido2.value = r[0].apellido2;

                fecha_nacimiento.value = r[0].fecha_nacimiento;
                sexo.value = r[0].sexo;
                e_civil.value = r[0].estado_civil;
                domicilio.value = r[0].domicilio;
                telef_domicilio.value = r[0].telef_domicilio;
                celular.value = r[0].celular;
                correo.value = r[0].correo;

                //console.log(r);
                var info = document.getElementById('info');
                if (r.length != 0) {
                    info.style.display = 'block';
                    info.innerHTML = r[0].nombre1 + ' ' + r[0].apellido1 + ' - <strong class="text-dark">HISTORIAL CLINICO(' + r[0].cod_historial + ')</strong> - FECHA REALISADA(' + r[0].fecha_ingreso + ')';
                    document.getElementById('cod_paciente').value = ''
                } else {
                    alert('no')
                    info.style.display = "none";
                    info.innerHTML = '';
                }
            }else{
                nombre1.value = '';
                nombre2.value = '';
                apellido1.value = '';
                apellido2.value = '';

                fecha_nacimiento.value = '';
                sexo.value = '';
                e_civil.value = '';
                domicilio.value = '';
                telef_domicilio.value = '';
                celular.value = '';
                correo.value = '';
            }


        }
    });
}

get_Session_Cod();
function get_Session_Cod() {
    var session_cod = document.getElementById('cod_paciente').value;
    // alert(session_cod);
    var parametros = {
        "cod_agenda": session_cod,
    }
    if (parseInt(session_cod) > 0) {
        $.ajax({
            data: parametros,
            url: 'buscar_paciente_admin_agenda',
            type: 'POST',
            dataType: 'JSON',
            success: function (r) {
                //`cod_agenda`, `nombre1`, `apellido1`, `telf`, `cod_doctor`, `fecha_cita`, `hora`, `observacion`, `confir`
                nombre1.value = r.nombre1;
                apellido1.value = r.apellido1;
                celular.value = r.telf;

            }
        });

    }
}


