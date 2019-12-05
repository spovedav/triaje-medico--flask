from flask import Flask, render_template,session, request ,redirect,g,url_for,flash
import os,json,datetime
from datetime import date #dia actutal
from bd_web.conection import conn, conexion
from datetime import date
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.secret_key = os.urandom(24)

#SocketIO -> Modulo que permite hacer la conexion
#app -> conexion al servidor
socketio = SocketIO(app) #variable que la conexion socket

#global variabale_globar = "ALMACENA VARIABLE GLOBAL"

@app.route('/login')
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #session.pop('user',None)
        try:
            with conn.cursor() as cursor:
                passw = request.form['passlogin']
                userr = request.form['userlogin']
                print(passw)
                #user = request.post('user')
                sql="SELECT count(*) as total FROM usuarios WHERE nickname='{}' AND pass='{}'".format(str(userr),str(passw))
                cursor.execute(sql)
                result=cursor.fetchone()
                verdad = result['total']
                if verdad == 1:
                    session['user']=request.form['userlogin']
                    g.user = session['user']
                    return redirect(url_for('menu'))
                    # return render_template('menu.html',userSession = session['user'])
                else:
                    return render_template('login.html',message="Usuario inocrrecto")
                    conn.close()

        finally:
            pass
            # conn.close()
    return render_template('login.html',message="")

@app.route('/imagen_user', methods=['GET', 'POST'])
def imagen_user():
    global nombre_imagen
    global doctor
    nombre_imagen = ''
    if request.method == 'POST':
        #session.pop('user',None)
        try:
            with conn.cursor() as cursor:
                passw = request.form['passlogin']
                userr = request.form['userlogin']
                print(passw)
                #user = request.post('user')
                sql="SELECT imagen, nombre1, apellido1 FROM usuarios WHERE nickname='{}' AND pass='{}'".format(str(userr),str(passw))
                cursor.execute(sql)
                result=cursor.fetchone()
                nombre_imagen = result['imagen']
                doctor = result['nombre1']+ ' '+result['apellido1']
            return str(nombre_imagen)
        finally:
            pass
    
@app.route('/menu')
def menu():
    if g.user:
        return render_template('menu.html',userSession=session['user'],nombre_imagen=nombre_imagen,doctor=doctor)
        g.user = session['user']
    #return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
    return redirect(url_for('login'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/getsesssion')
def getsesssion():
    if 'user' in session:
        return session['user']

    return ' No Logged in'
        

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    session.pop('cod', None)
    session.pop('nickname',None)
    #return redirect(url_for('login'))
    # conn.close()
    return render_template('login.html')

@app.route('/agendar', methods=['GET', 'POST'])
def agendar():
    #Día actual
    fecha_actual = date.today()

    if g.user:
        try:
            with conn.cursor() as cursor:
                SQL="SELECT * FROM agendar where fecha_cita=%s"
                cursor.execute(SQL,(fecha_actual))
                result=cursor.fetchall()
                #result= json.dumps(result)
                return render_template('agendar.html',userSession=session['user'], result=result,nombre_imagen=nombre_imagen)
        finally:
            pass#conn.close()
    else:
        return redirect(url_for('login'))

#------------  FUNCIONES DE AGENDAR ------------------
@app.route('/insert_paciente', methods=['POST'])
def insert_paciente():
    if request.method == 'POST':
        try:
            with conn.cursor() as cursor:
                cod_paciente = request.form['cod_paciente']
                
                #cedula = request.form['cedula'] - esto es un requisito
                nombre1 = request.form['nombre1']
                apellido1 = request.form['apellido1']
                telf = request.form['telf']
                medico = request.form['medico']
                fecha = request.form['fecha']
                hora = request.form['hora']
                obse = request.form['observacion']
                if cod_paciente=="":
                    # REGISTRO EN BASQ DE DATOS 
                    sql="INSERT INTO `agendar`(`cod_agenda`, `nombre1`, `apellido1`, `telf`, `cod_doctor`, `fecha_cita`, `hora`, `observacion`, `confir`) VALUES (null,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql,(nombre1,apellido1,telf,medico,fecha,hora,obse,'False'))
                    #result=cursor.fetchone()
                    conn.commit()
                else:
                    sql="UPDATE `agendar` set nombre1=%s, apellido1=%s, telf=%s, cod_doctor=%s, fecha_cita=%s, hora=%s, observacion=%s where cod_agenda=%s"
                    cursor.execute(sql,(nombre1,apellido1,telf,medico,fecha,hora,obse,cod_paciente))
                    conn.commit()
        finally:
            pass
    return redirect(url_for('agendar'))

@app.route('/confir', methods=['POST'])
def confir():
    # valor = False
    num = 0
    if request.method == 'POST':
        try:
            with conn.cursor() as cursor:
                cod_paciente = request.form['cod']
                if request.form['valor']=='true':
                    sql="UPDATE `agendar` set confir=%s where cod_agenda=%s"
                    cursor.execute(sql,(1,int(cod_paciente)))
                    num = 1
                else:
                    # UPDATE `agendar` SET `confir`=0 WHERE cod_agenda = 16
                    sql="UPDATE `agendar` set confir=%s where cod_agenda=%s"
                    cursor.execute(sql,(0,int(cod_paciente)))
                    num = 1
                

                # sql="UPDATE `agendar` set confir=%s where cod_agenda=%s"
                # cursor.execute(sql,(valor,cod_paciente))
                conn.commit()
            return str(num)
        finally:
            pass

@app.route('/rrellenarTabla', methods=['POST'])
def rrellenarTabla():
    if request.method == 'POST':
        fecha_actual = request.form['fecha']
    # else:
        # fecha_actual = date.today()

    try:
        with conn.cursor() as cursor:
            SQL="SELECT cod_agenda,nombre1,apellido1,telf,cod_doctor,hora,confir from agendar where fecha_cita=%s"
            cursor.execute(SQL,(fecha_actual))
            result=cursor.fetchall()
            # for valor in result:
            #     pass
        return json.dumps(result)
    finally:
        pass

#- funcion que recibe un parametro Eliminar-
@app.route('/aciones', methods=['POST'])
def aciones():
    if request.method == 'POST':
        cod = request.form['cod']
        bandera = request.form['bandera']

    if(bandera=="delete"):
        try:
            with conn.cursor() as cursor:
                SQL="DELETE FROM agendar where cod_agenda=%s"
                cursor.execute(SQL,(int(cod)))
                conn.commit()
            return json.dumps(1) 
        finally:
            pass

    if(bandera=="update"):
        with conn.cursor() as cursor:
            SQL="SELECT cod_agenda,nombre1,apellido1,telf,cod_doctor,hora,observacion FROM agendar where cod_agenda=%s"
            cursor.execute(SQL,(int(cod)))
            result=cursor.fetchone()
            # for re in result:
            #     pass
        return json.dumps(result)
    pass



@app.route('/info', methods=['POST'])
def info():
    if request.method == 'POST':
        fecha_actual = request.form['fecha']
        
    with conn.cursor() as cursor:
        SQL="SELECT * from agendar where fecha_cita=%s"
        cursor.execute(SQL,(fecha_actual))
        result=cursor.fetchall()
        # valores = []
        # respuesta = []
        # for item in result:
        #     valores = tuple(item.values())
        #     respuesta.append(valores)
    return str(result)

#----------- END FUNCION AGENDAR --------------

# ///////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////
#------------ FUNCIONES DE ADMISION ------------
@app.route('/admision')
def admision():
    if 'cod' in session:
        pass# session['cod'] = ''
    else:
        session['cod'] = ''

    if g.user:
        hoy=date.today()
        if 'cod' in session:
            codi = session['cod']
        else:
            codi = 'null'
        return render_template('admision.html',userSession=session['user'], fecha=hoy,codigo=codi,nombre_imagen=nombre_imagen)
    else:
        return redirect(url_for('login'))


@app.route('/cod', methods=['POST'])
def cod_():
    if request.method == 'POST':
        codigo = request.form['cod']
        g.cod = codigo
        global codi
        codi=g.cod
        session['cod']=codi
    return g.cod
    # return redirect(url_for('admision'))

@app.route('/crud_admision', methods=['POST'])
def crud_admision():
    SQL = ''
    global control_admin
    global control_historial
    global anoAcutal
    global cod_historial_clinico
    # accion = ''
    fecha = datetime.datetime.now()
    anoAcutal = fecha.year
    # cod_historial_clinico = 0
    if request.method == 'POST':
        try:
            with conn.cursor() as cursor:
                SQL=''
                result=''
                SQL = "SELECT año as ano FROM `control_`"
                cursor.execute(SQL)
                result = cursor.fetchone()
                BD_ano = result['ano']
                if (str(BD_ano)!=(str(anoAcutal))):
                    SQL=''
                    SQL="UPDATE `control_` SET `año`=%s,control_admin=%s"
                    cursor.execute(SQL,(anoAcutal,0))
                    conn.commit()
                
                SQL=''
                result=''
                SQL="SELECT control_admin as admin, control_historial as histo FROM `control_` LIMIT 1"
                cursor.execute(SQL)
                result=cursor.fetchone()
                control_admin = result['admin']
                control_historial = result['histo']

                SQL=''
                SQL="UPDATE `control_` SET `control_admin`=%s"
                cursor.execute(SQL,(int(control_admin)+1))
                conn.commit()
                
                bandera = request.form['bandera']
                if (bandera == "insert"):
                    with conn.cursor() as cursor:
                        cod_agenda= request.form['cod_agenda']
                        cedula = request.form['cedula']
                        fecha_nacimiento = request.form['fecha_nacimiento']
                        nombre1 = request.form['nombre1']
                        nombre2 = request.form['nombre2']
                        apellido1 = request.form['apellido1']
                        apellido2 = request.form['apellido2']
                        sexo = request.form['sexo']
                        e_civil = request.form['e_civil']
                        domicilio = request.form['domicilio']
                        telef_domicilio = request.form['telef_domicilio']
                        celular = request.form['celular']
                        correo = request.form['correo']
                        fecha_ingreso = request.form['fecha_ingreso']
                        
                        
                        SQL=''
                        result = ''
                        SQL="SELECT COUNT(*) as co FROM `admision` WHERE cedula='{}'".format(cedula)
                        cursor.execute(SQL)
                        result=cursor.fetchone()
                        if(int(result['co'])>0):
                            SQL=''
                            result = ''
                            SQL="SELECT cod_historial as c FROM `admision` WHERE cedula='{}'".format(cedula)
                            cursor.execute(SQL)
                            result=cursor.fetchone()
                            cod_historial_existenete = result['c']
                            #si el numero de cedula tiene un historial clinico se le admisiona con el mismo
                            cod_historial_clinico = cod_historial_existenete
                        else:
                            SQL=''
                            SQL="UPDATE `control_` SET `control_historial`=%s"
                            cursor.execute(SQL,(int(control_historial)+1))
                            conn.commit()
                            cod_historial_clinico = control_historial + 1
                            pass                            
                
                        SQL_INSERT=''
                        SQL_INSERT="INSERT INTO `admision`(`cod_historial`,`cod_agenda`,`nombre1`,`nombre2`, `apellido1`,`apellido2`,`cedula`, `fecha_nacimiento`,`sexo`, `estado_civil`, `domicilio`, `telef_domicilio`,`celular`, `correo`, `fecha_ingreso`,`ADMISION`) VALUES ({},{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(int(cod_historial_clinico),int(cod_agenda),nombre1,nombre2,apellido1,apellido2,cedula,fecha_nacimiento,sexo,e_civil,domicilio,telef_domicilio,celular,correo,fecha_ingreso,str(control_admin+1)+'-'+str(anoAcutal))
                        cursor.execute(SQL_INSERT)
                        conn.commit()
                        cod_historial_clinico = ''

                    if (bandera == "update"):
                        pass

                    if (bandera == "delete"):
                        pass

                return str(1)
        except:
            return str(SQL_INSERT)
            # return str(str(control_historial)+'-'+(str(control_admin)+'-'+str(anoAcutal))+'-'+nombre1+'-'+nombre2+'-'+apellido1+'-'+apellido2+'-'+cedula+'-'+fecha_nacimiento+'-'+sexo+'-'+e_civil+'-'+domicilio+'-'+telef_domicilio+'-'+celular+'-'+correo+'-'+fecha_ingreso)
        finally:
            pass


@app.route('/buscar_paciente_admin', methods=['POST'])
def buscar_paciente_admin():
    if request.method == "POST":
        try:
            cedula = request.form['buscar']
            with conn.cursor() as cursor: #cedula > `fecha_nacimiento`
                SQL="SELECT `cod_historial`, `nombre1`, `nombre2`, `apellido1`, `apellido2`, `cedula`, `sexo`, `estado_civil`, `domicilio`, `telef_domicilio`, `celular`, `fecha_nacimiento`, `correo`, `fecha_ingreso`  FROM `admision` where cedula='{}' ORDER BY fecha_ingreso ASC LIMIT 1".format(str(cedula))
                cursor.execute(SQL)
                result=cursor.fetchall()
                return json.dumps(result)
                # return str(result)
        finally:
            pass


@app.route('/buscar_paciente_admin_agenda', methods=['POST'])
def buscar_paciente_admin_agenda():
    SQL=''
    result=''
    if request.method == "POST":
        try:
            cod_agenda = request.form['cod_agenda']
            with conn.cursor() as cursor: #cedula > `fecha_nacimiento`
                SQL="SELECT `cod_agenda`, `nombre1`, `apellido1`, `telf`, `cod_doctor`, `fecha_cita`, `hora`, `observacion`, `confir` FROM `agendar` WHERE cod_agenda={} LIMIT 1".format(int(cod_agenda))
                cursor.execute(SQL)
                result=cursor.fetchone()
                return json.dumps(result)
                # return str(result)
        finally:
            pass

@app.route('/rellenar_table_admision')
def rellenar_table_admision():
    fecha_actual = date.today()
    try:
        with conn.cursor() as cursor:
            SQL="SELECT `cod_paciente`, `cod_historial`, `nombre1`, `nombre2`, `apellido1`, `apellido2`, `cedula`, `ADMISION`, `fecha_ingreso` FROM `admision` WHERE fecha_ingreso='{}'".format(str(fecha_actual))
            cursor.execute(SQL)
            result=cursor.fetchall()
        return json.dumps(result)
    finally:
        pass
#----------- END FUNCIONES DE ADMISION ---------------


# ////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////
#----------- FUNCIONES DE PANEL PRINCIPAL --------------
@app.route('/panel_principal')
def panel_principal():
    if g.user:
        return render_template('panel_principal.html',userSession=session['user'],nombre_imagen=nombre_imagen)
    else:
        redirect(url_for('login'))
    
    return render_template('login.html')
#----------- END FUNCION DEL PANEL PRINCIPAL ----------------

# /////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////
#------------- FUNCIONE DE EVOLCUCION ----------------
@app.route('/evolcuion')
def evolucion():
    if g.user:
        return render_template('evolucion.html', userSession=session['user'],nombre_imagen=nombre_imagen)
    else:
        return redirect(url_for('login'))

#------------- END FUNCION DE EVOLUCION ---------------


# //////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////
""" Funcion es de Socketio """
# *** agenda ***
@socketio.on('cliente_row')
def cliente_row(cod):
    #send(cod, broadcast = True)
    socketio.emit('response',cod)
    # print("Codigo -> "+cod)
    #return cod

@socketio.on('panel')
def all_panel():
    fecha_actual = date.today()
    try:
        with conn.cursor() as cursor:
            SQL="SELECT ag.cod_agenda,CONCAT(usu.nombre1,' ',usu.apellido1,' - ESPESIALIDAD') as doctor,ad.cod_paciente,ag.hora, ad.cod_historial, ad.nombre1, ad.nombre2, ad.apellido1, ad.apellido2, ad.cedula, ad.ADMISION, ad.fecha_ingreso FROM admision ad INNER JOIN agendar ag on (ad.cod_agenda = ag.cod_agenda) INNER JOIN usuarios usu on (usu.cod_doctor = ag.cod_doctor)  WHERE fecha_ingreso='{}' ORDER by ag.hora,ad.nombre1+' '+ad.apellido1".format(str(fecha_actual))
            cursor.execute(SQL)
            result=cursor.fetchall()
            jsonn = json.dumps(result)
            socketio.emit('response',result)
        # return str(result)
        # return json.dumps(result)
    finally:
        pass

    # socketio.emit('response',json)

# *** end agenda ***
#----------------------
# *** panel principal ***

# *** end panel ***


if __name__ == '__main__':
    app.run(debug=True)
 
