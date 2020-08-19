"use strict";

$('#get-template').on('submit', (evt) => {
  evt.preventDefault();

  const selectedId = $('#template-id').val();

  $.get(`/api/template/${selectedId}`, (res) => {
    $('#templatename').html(res.templatename);
    $('#createdby').html(res.createdby);
    $('#createdon').html(res.createdon);
  });
});

// $('#get-checklist').on('submit', (evt) => {
//   evt.preventDefault();

//   const selectedId = $('#checklist-id').val();

//   $.get(`/api/checklist/${selectedId}`, (res) => {
//     $('#templatename').html(res.templatename);
//     $('#timeframe').html(res.timeframe);
//     $('#whofor').html(res.whofor);
//   });
// });

