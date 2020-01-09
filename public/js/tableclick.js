$('#deleteModal').on('show.bs.modal', function(event) {
  var button = $(event.relatedTarget);
  var id = button.data('id');
  var name = button.data('name');
  var classname = button.data('classname');
  var modal = $(this);
  var text_base = 'Tem certeza que deseja deletar, ';
  var base_url = 'http://127.0.0.1:8000/'; 
  modal.find('.modal-content h3').text(text_base.concat(name).concat('?'));
  modal.find('.btn-primary').attr('href',base_url.concat(classname).concat('/delete/').concat(id))
  });