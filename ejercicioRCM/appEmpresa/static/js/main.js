$(document).ready(function () {

    //Se inicializan los selects
    var $regiones = $("#regiones");
    var $provincias = $("#provincias");
    var $comunas = $("#comunas");

    // Al cambiar el select de regiones, llama a la funcion getProvincias para obtener la provincia correspondiente
    $("#regiones").change(function(){
        var regionId = document.getElementById("regiones").selectedIndex;
        regionId = regionId - 1;
        $('#provincias').empty();
        $provincias.append('<option id="-1">' + 'Seleccione...' + '</option>');
        $('#comunas').empty();
        $comunas.append('<option id="-1">' + 'Seleccione...' + '</option>');
        $("#div_prov").css("display","flex");
        getProvincias(regionId);
        $('#txt_region').val("");
        $('#txt_provincia').val("");
        $('#txt_comuna').val("");
        $('#txt_region').val(regionId);
    });

    // Al cambiar el select de provincias, llama a la funcion getComunas para obtener la comuna correspondiente
    $("#provincias").change(function(){ 
        var regionId = document.getElementById("regiones").selectedIndex;
        regionId = regionId - 1;
        var provinciaId = document.getElementById("provincias").selectedIndex;
        provinciaId = provinciaId - 1;
        $('#comunas').empty();
        $comunas.append('<option id="-1">' + 'Seleccione...' + '</option>');
        $("#div_com").css("display","flex");
        getComunas(regionId, provinciaId);
        $('#txt_provincia').val("");
        $('#txt_comuna').val("");
        $('#txt_provincia').val(provinciaId);
    });

    $("#comunas").change(function(){ 
        var comunaId = document.getElementById("comunas").selectedIndex;
        comunaId = comunaId - 1;
        $('#txt_comuna').val("");
        $('#txt_comuna').val(comunaId);
    });


    // Funcion que recupera las regiones en formato JSON
    $.getJSON('/static/js/comunas-regiones.JSON', function(data){
        
        for (var i = 0; i < data['regiones'].length; i++){
            $regiones.append('<option id="' + i + '">' + data['regiones'][i]['region'] + '</option>');
        }
        console.log(data);
    });

    // Funcion que recupera las provincias en formato JSON
    function getProvincias(regionId){
        $.getJSON('/static/js/comunas-regiones.JSON', function(data){
            
    
            for (var i = 0; i < data['regiones'][regionId]['provincias'].length; i++){
                $provincias.append('<option id="' + i + '">' + data['regiones'][regionId]['provincias'][i]['name'] + '</option>');
            }
            console.log(data);
        });  
    }

    // Funcion que recupera las comunas en formato JSON
    function getComunas(regionId, provinciaId){
        $.getJSON('/static/js/comunas-regiones.JSON', function(data){
            
            
            for (var i = 0; i < data['regiones'][regionId]['provincias'][provinciaId]['comunas'].length; i++){
                $comunas.append('<option id="' + i + '">' + data['regiones'][regionId]['provincias'][provinciaId]['comunas'][i]['name'] + '</option>');
            }
            console.log(data);
        });
    }


});

function validador(e){
    var indexReg = document.getElementById("regiones").selectedIndex;
    if(indexReg == 0){
      alert("Por favor escoja una región");
      e.preventDefault();
      return;
    }
    var indexProv = document.getElementById("provincias").selectedIndex;
    if(indexProv == 0){
      alert("Por favor escoja una provincia");
      e.preventDefault();
      return;
    }
    var indexCom = document.getElementById("comunas").selectedIndex;
    if(indexCom == 0){
      alert("Por favor escoja una comuna");
      e.preventDefault();
      return;
    }
    
}