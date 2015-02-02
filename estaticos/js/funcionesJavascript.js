//Permisos
//	Despliegue de modales
$(document).on('show.bs.modal', '#crearPermisos', function (event) {
 	var button = $(event.relatedTarget)
 	var url = button.data('url') 
 	$.ajax({ 
 	    type: $(this).attr('method'),
 	    url: url, 
 	    success: function(data, status) {
 	    	$('#modalPermisos').html(data);
 	    }
 	});
 });

$(document).on('show.bs.modal', '#editarPermiso', function (event) {
	var button = $(event.relatedTarget) 
	var id = button.data('id')
	var pag = button.data('pag')
	var url = '/permisos/' + pag +'/editar/' + id + '/'

	$.ajax({ 
		type: $(this).attr('method'),
		url: url, 
		success: function(data, status) {
			$('#modalEditarPermisos').html(data);
		}
	});
});
  
$(document).on('show.bs.modal', '#verPermiso', function (event) {
	var button = $(event.relatedTarget) 
	var id = button.data('id')
	var pag = button.data('pag')
	var url = '/permisos/' + pag +'/ver/' + id + '/'

	$.ajax({ 
		type: $(this).attr('method'),
	    url: url, 
	    success: function(data, status) {
	    	$('#modalVerPermisos').html(data);
	    }
	});
});
 
 $(document).on("click", "#eliminarPermisoButton", function () {
	 var url = $(this).attr('data-url')
	 $.ajax({ 
		 type: $(this).attr('method'), 
	     url: url, 
	     data: $(this).serialize(),
	     success: function(data, textStatus) {
	    	 $('#eliminarPermiso').modal('hide')
	    	 index = data.indexOf('<!-- Inicio del cuerpo -->')
	    	 data_slice = data.slice(index)
	    	 index = data_slice.indexOf('<!-- Fin del cuerpo -->')
	    	 data_slice = data_slice.slice(0, index)
	    	 $('#inicio').html(data_slice);
	     }
	 });
	 return false;
});

//	Codigo para ejecutar la logica del negocio
$(document).on("click", "#permisos", function () {
	var id = $(this).data('id');
	var pag = $(this).data('pag');
	var nombre = $(this).data('nombre')
	var url = '/permisos/' + pag + '/eliminar/' + id + '/'
	$('.modal-body').html( 'Esta seguro de que desea eliminar el permiso ' + '<strong>' + nombre + '</strong>' + '?' + '<p class="text-warning"><small>Si lo haces, todos sus datos se eliminarán permanentemente.</small></p>')
	$('#eliminarPermisoButton').attr("data-url", url);
});

$(document).on("click", "#roles", function () {
	var id = $(this).data('id');
	var pag = $(this).data('pag');
	var nombre = $(this).data('nombre')
	var url = '/roles/' + pag + '/eliminar/' + id + '/'
	$('.modal-body').html( 'Esta seguro de que desea eliminar el Rol ' + '<strong>' + nombre + '</strong>' + '?' + '<p class="text-warning"><small>Si lo haces, todos sus datos se eliminarán permanentemente.</small></p>')
	$('#eliminarRolButton').attr("data-url", url);
});

//Roles
$(document).on('show.bs.modal', '#crearRoles', function (event) {
 	var button = $(event.relatedTarget)
 	var url = button.data('url') 
 	$.ajax({ 
 	    type: $(this).attr('method'),
 	    url: url, 
 	    success: function(data, status) {
 	    	$('#modalRoles').html(data);
 	    }
 	});
 });

$(document).on("click", "#eliminarRolButton", function () {
	 var url = $(this).attr('data-url')
	 $.ajax({ 
		 type: $(this).attr('method'), 
	     url: url, 
	     data: $(this).serialize(),
	     success: function(data, textStatus) {
	    	 $('#eliminarRol').modal('hide')
	    	 index = data.indexOf('<!-- Inicio del cuerpo -->')
	    	 data_slice = data.slice(index)
	    	 index = data_slice.indexOf('<!-- Fin del cuerpo -->')
	    	 data_slice = data_slice.slice(0, index)
	    	 console.log(data_slice)
	    	 $('#inicio').html(data_slice);
	     }
	 });
	 return false;
});