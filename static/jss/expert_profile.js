$(function(){
    var expert = $(".expert-title").find('.inner');

    expert.click(function(){
        $(this).parent().parent().parent().parent().find(".profile-togglable").toggle();
    });
});
