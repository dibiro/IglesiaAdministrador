function buscar_versiculos_por_filtrado() {
  $.ajax({
    url: '/Culto/buscar_versiculos_por_filtrado/',
    type: 'GET',
    dataType: 'json',
    data: {libro: $('#libro').val(),
    	   capitulo: $('#capitulo').val(),
           desde: $('#Desde').val(),
           hasta: $('#Hasta').val(),
           id: $('#id_culto').val()
          },
  })
  .done(function(data) {
    $('#contenido').empty();
    $.each(data, function(index, val) {
      $('#contenido').append('<li class="list-group-item"><span class="badge">'+val.versiculo+'</span>'+val.texto+'</li>');
    });
  })
  .fail(function() {
  })
  .always(function() {
  });
}