(function() {
  var expert_pk;

  expert_pk = null;

  window.runRequestSOModal = function(pk) {
    var min_height;
    expert_pk = pk;
    min_height = 0;
    return $('#soModal').modal().on('shown.bs.modal', function() {
      var about_so, div, h, i, len, li, ref;
      about_so = $('.modal-so-request').find('.about-so');
      ref = about_so.find('li');
      for (i = 0, len = ref.length; i < len; i++) {
        li = ref[i];
        div = $(li).find('div');
        div = $(div);
        console.log(div);
        console.log(div.height());
        if (div.height() > min_height) {
          min_height = div.height();
        }
      }
      h = about_so.find('h3').height();
      about_so.css('min-height', min_height + h * 6 + 'px');
      return console.log(min_height);
    });
  };

  window.openSoPage = function() {
    return location.href = "http://hygeiais.com/so/experts/" + expert_pk;
  };

}).call(this);
