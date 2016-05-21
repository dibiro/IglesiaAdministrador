var dato_anterior = {
            'tipo':'',
            'libro':'',
            'capitulo':'',
            'desde':'',
            'hasta':'',
            'selecionados':'',
            'selecionados':'',
        }

function buscar_versiculos_por_filtrado() {
  $.ajax({
    url: '/Culto/espectador_de_culto/',
    type: 'GET',
    dataType: 'json',
    data: {culto: $('#id_culto').val(),
          },
  })
  .done(function(data) {
    if (dato_anterior.fecha!=data.fecha) {
      $('#contenedor').empty();
      if (data.tipo==1) {
        $("#title").html('<h1 class="text-center" >'+data.libro+' '+data.capitulo+': '+data.desde+'-'+data.hasta+'</h1>')
        $.each(data.selecionados, function(index, val) {
          $('#contenedor').append('<ul class="animated fadeInUp list-group col-sm-10 col-xs-10 col-sm-offset-1 col-xs-offset-1 col-md-offset-1 col-md-10" id="contenido"><li class="list-group-item"><span class="badge">'+val.versiculo+'</span>'+val.texto+'</li></ul>');
        });
      }
      dato_anterior=data;
    }
  })
  .fail(function() {
  })
  .always(function() {
  });
}

setInterval(buscar_versiculos_por_filtrado, 1000)