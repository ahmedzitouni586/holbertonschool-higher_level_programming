$.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: (r) => {
      $('#hello').text(r.hello);
    }
});
