"use strict";

$('#get-user').on('submit', (evt) => {
  evt.preventDefault();

  const selectedId = $('#user-id').val();

  $.get(`/api/user/${selectedId}`, (res) => {
    $('#username').html(res.username);
    $('#email').html(res.email);
    $('#usertype').html(res.usertype);
  });
});

