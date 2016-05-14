$("select").select2({dropdownAutoWidth: 'true'});

function Calendario(year, mouth) {
  $.ajax({
    url: 'calendario/',
    type: 'GET',
    dataType: 'json',
    data: {year: year, mouth: mouth},
  })
  .done(function(data) {
    $('#calendario').empty();
    var texto = '';
    $.each(data, function(index, val) {
    		if (val.weekday=='0') {
    			texto += '<tr><th class="';
    			if (val.culto=='1' || val.evento=='1') {
    				texto += 'success';
    			};
    			texto += '">'+val.dia+' ';
    			if (val.culto=='1') {
    				texto += ' <i class="fa fa-hospital-o culto" data-id="'+val.id_culto+'" aria-hidden="true"></i>';
    			};
    			if (val.evento=='1') {
    				texto += ' <i class="fa fa-hospital-o evento" data-id="'+val.id_evento+'" aria-hidden="true"></i>';
    			};
    			texto += '</th>'
      			$('#calendario').html(texto);
    		}else if (val.weekday=='6') {
    			texto += '<th class="';
    			if (val.culto=='1' || val.evento=='1') {
    				texto += 'success';
    			};
    			texto += '">'+val.dia+' ';
    			if (val.culto=='1') {
    				texto += ' <i class="fa fa-hospital-o culto" data-id="'+val.id_culto+'" aria-hidden="true"></i>';
    			};
    			if (val.evento=='1') {
    				texto += ' <i class="fa fa-hospital-o evento" data-id="'+val.id_evento+'" aria-hidden="true"></i>';
    			};
    			texto += '</th></tr>'
      			$('#calendario').html(texto);
    		}else {
    			texto += '<th class="';
    			if (val.culto=='1' || val.evento=='1') {
    				texto += 'success';
    			};
    			texto += '">'+val.dia+' ';
    			if (val.culto=='1') {
    				texto += ' <i class="fa fa-hospital-o culto" data-id="'+val.id_culto+'" aria-hidden="true"></i>';
    			};
    			if (val.evento=='1') {
    				texto += ' <i class="fa fa-hospital-o evento" data-id="'+val.id_evento+'" aria-hidden="true"></i>';
    			};
    			texto += '</th>'
      			$('#calendario').html(texto);
    		};
				
    });
  })
  .fail(function() {
  })
  .always(function() {
  });
}

$("#year").change(function(event) {
    Calendario($("#year").val(), $("#mes").val())
});
$("#mes").change(function(event) {
    Calendario($("#year").val(), $("#mes").val())
});

Calendario($("#year").val(), $("#mes").val());

$('.datetimepicker').datetimepicker({format: "YYYY-MM-DD",locale: 'es',});

function crear_culto() {
    $.ajax({
    url: 'crear_culto/',
    type: 'POST',
    dataType: 'json',
    data: {
        'fecha': $("#Fecha").val(),
        'Direccion': $("#Direccion").val(),
        'lectura': $("#Lectura").val(),
        'recolecion': $("#Recolecion").val(),
        'oracion': $("#Oracion").val(),
        'coros': $("#Coros").val(),
        'predicacion': $("#Predicacion").val(),
        'tipo': $("#tipos_de_cultos").val(),
    },
    beforeSend: function(xhr) {xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));},
  })
  .done(function(data) {
	Calendario(data.year, data.month)
  })
  .fail(function() {
  })
  .always(function() {
  });
}

$("#crear_culto_btn").click(function(event) {
    crear_culto();
    $('#crear_culto').modal('hide');
});