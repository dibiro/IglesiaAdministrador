$("select").select2({dropdownAutoWidth: 'true'});

function llenar_select(select, desde, hasta, valor) {
	$('#'+select).empty();
	for (var i = desde; i <= hasta; i++) {
		$('#'+select).append($('<option>', {
	        value: i,
	        text: i
        }));
  };
  $('#'+select).select2('val',valor);
}


function buscar_versiculos_por_capitulo(libro, capitulo, iflibro) {
  $.ajax({
    url: 'buscar_versiculos_por_capitulo/',
    type: 'GET',
    dataType: 'json',
    data: {libro: libro, capitulo: capitulo},
  })
  .done(function(data) {
    $('#contenido').empty();
    $.each(data.versiculos, function(index, val) {
      $('#contenido').append('<li class="list-group-item"><span class="badge">'+val.versiculo+'</span>'+val.texto+'</li>');
    });
    if (iflibro) {
      llenar_select('capitulo', 1, data.numero_capitulos, '1');
    }
    llenar_select('Desde', 1, data.numero_versiculos, '1');
    llenar_select('Hasta', 1, data.numero_versiculos, '1');
  })
  .fail(function() {
  })
  .always(function() {
  });
}

function buscar_versiculos_por_filtrado() {
  $.ajax({
    url: 'buscar_versiculos_por_filtrado/',
    type: 'GET',
    dataType: 'json',
    data: {libro: $('#libro').val(), capitulo: $('#capitulo').val(), desde: $('#Desde').val(), hasta: $('#Hasta').val()},
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

$('#libro').change(function(event) {
  llenar_select('capitulo', 1, $("#libro").find(":selected").data("capitulos"), '1');
  buscar_versiculos_por_capitulo($('#libro').val(), 1, true)
});

$('#capitulo').change(function(event) {
  buscar_versiculos_por_capitulo($('#libro').val(), $('#capitulo').val(), false)
});

$('#filtrar').click(function(event) {
  buscar_versiculos_por_filtrado();
});