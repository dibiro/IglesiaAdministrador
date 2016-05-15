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
    				texto += ' <i class="fa fa-hospital-o fa-5 culto" data-toggle="modal" data-target="#modificar_culto" data-id="'+val.id_culto+'" aria-hidden="true"></i>';
    			};
    			if (val.evento=='1') {
    				texto += ' <i class="fa fa-hospital-o fa-5 evento" data-toggle="modal" data-target="#modificar_evento" data-id="'+val.id_evento+'" aria-hidden="true"></i>';
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
    				texto += ' <i class="fa fa-hospital-o fa-5 culto" data-toggle="modal" data-target="#modificar_culto" data-id="'+val.id_culto+'" aria-hidden="true"></i>';
    			};
    			if (val.evento=='1') {
    				texto += ' <i class="fa fa-hospital-o fa-5 evento" data-toggle="modal" data-target="#modificar_evento" data-id="'+val.id_evento+'" aria-hidden="true"></i>';
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
    				texto += ' <i class="fa fa-hospital-o fa-5 culto" data-toggle="modal" data-target="#modificar_culto" data-id="'+val.id_culto+'" aria-hidden="true"></i>';
    			};
    			if (val.evento=='1') {
    				texto += ' <i class="fa fa-hospital-o fa-5 evento" data-toggle="modal" data-target="#modificar_evento" data-id="'+val.id_evento+'" aria-hidden="true"></i>';
    			};
    			texto += '</th>'
      			$('#calendario').html(texto);
    		};
				
    });
  })
  .fail(function() {
  })
  .always(function() {
    add_evento();
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

function get_culto(id) {
    $.ajax({
    url: 'get_culto/',
    type: 'GET',
    dataType: 'json',
    data: {
        'id': id
    },
  })
  .done(function(data) {
    $("#id_culto").val(data.id);
    $("#Modificar_Fecha").val(data.Fecha);
    $("#Modificar_Direccion").select2('val', data.Direccion);
    $("#Modificar_Lectura").select2('val', data.Lectura);
    $("#Modificar_Recolecion").select2('val', data.Recolecion);
    $("#Modificar_Oracion").select2('val', data.Oracion);
    $("#Modificar_Coros").select2('val', data.Coros);
    $("#Modificar_Predicacion").select2('val', data.Predicacion);
    $("#Modificar_tipos_de_cultos").select2('val', data.tipos_de_cultos);
    $("#Modificar_Direccion").val(data.Direccion);
    $("#Modificar_Lectura").val(data.Lectura);
    $("#Modificar_Recolecion").val(data.Recolecion);
    $("#Modificar_Oracion").val(data.Oracion);
    $("#Modificar_Coros").val(data.Coros);
    $("#Modificar_Predicacion").val(data.Predicacion);
    $("#Modificar_tipos_de_cultos").val(data.tipos_de_cultos);
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

function add_evento() {
    $(".culto").click(function(event) {
        get_culto($(this).data('id'));
    });
}