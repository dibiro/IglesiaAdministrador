$('.datetimepicker').datetimepicker({format: "YYYY-MM-DD",locale: 'es',});
$("select").select2();

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
    url: '/Culto/buscar_versiculos_por_capitulo/',
    type: 'GET',
    dataType: 'json',
    data: {libro: libro, capitulo: capitulo},
  })
  .done(function(data) {
    $('#contenido').empty();
    $.each(data.versiculos, function(index, val) {
      $('#contenido').append('<li class="list-group-item versiculos" data-id="'+val.id+'"><span class="badge">'+val.versiculo+'</span>'+val.texto+'</li>');
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
    add_evento();
  });
}

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
      $('#contenido').append('<li class="list-group-item versiculos" data-id="'+val.id+'"><span class="badge">'+val.versiculo+'</span>'+val.texto+'</li>');
    });
  })
  .fail(function() {
  })
  .always(function() {
    add_evento();
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

$(window).on('resize', function(event) {
  $("#contenedor").css("height", window.innerHeight-$("nav").height()-100 -$("div_1").height() + "px");
  $("#chat").css("height", window.innerHeight-$("nav").height() + "px");
});
  $("#contenedor").css("height", window.innerHeight-$("nav").height()-100 -$("div_1").height() + "px");
  $("#chat").css("height", window.innerHeight-$("nav").height() + "px");

function seleccionar_versiculo(id) {
  $.ajax({
    url: '/Culto/seleccionar_versiculo/',
    type: 'GET',
    dataType: 'json',
    data: {id: id, id_culto: $('#id_culto').val()},
  })
  .done(function(data) {
  })
  .fail(function() {
  })
  .always(function() {
  });
}

function add_evento() {
  $('.versiculos').click(function(event) {
    seleccionar_versiculo($(this).data('id'))
  });
}