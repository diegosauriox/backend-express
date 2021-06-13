const { sendResponse } = require('../utils/responseHandler');
const { mysql } = require('../_config/mysql')

const datosCtrl={}

datosCtrl.createData = async (req, res) => {
    const {dia, mes, año, fecha, region, id_volcan, hr_reporte, hr_evento, tipo_evento,
         ml, dr,prof, tiempo_generar_reporte, comentarios, id_nivel_alerta, reav_y_doc } = req.body;
    mysql.query('insert into evento (dia,mes,año,fecha,region,id_volcan, hr_report, hr_evento, tipo_evento'+
     'ml, dr,prof,tiempo_generar_reporte,comentarios, id_nivel_alerta, reav_y_doc)'+
     'Values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'+
     'commit;',
     [dia, mes, año, fecha, region, id_volcan, hr_reporte, hr_evento, tipo_evento,
        ml, dr,prof, tiempo_generar_reporte, comentarios, id_nivel_alerta, reav_y_doc
     ],(error,results)=>{
         if(error){
             sendResponse(res,true,"Taskfailded",error)
         }else{
             sendResponse(res,false,"Success",results)
         }
     }

     )
    }
    module.exports = datosCtrl;