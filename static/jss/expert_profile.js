$(function(){
    var expert = $(".expert-title");
    
    expert.click(function(){
        $(this).parent().parent().parent().find(".profile-togglable").toggle();
    });
});
