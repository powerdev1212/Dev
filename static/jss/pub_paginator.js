$(document).ready(function(){
    var page_size = 10;
    var page_start = 1;
    var container = $("#pag-right");
    var pub_rows = $(".pub-row").length;

    function generatePaginator(){
        generatePages();
        setActive(1);
        appendPrevButton();
        appendNextButton();
        hideButtons();
        showPage();
    };

    function generatePages(){
        var pages = getPages();
        for(p=1;p<=pages;p++){
            var li = $("<li></li>");
            var link = $("<a></a>").attr("ident",p).html(p).css({"cursor": "pointer"}).appendTo(li);
            li.appendTo(container);
        };
    };

    function setActive(id){
        $("#pag-right li").removeClass("active");
        $("a[ident=" + id + "]").css({"cursor":"default"}).parent().addClass("active");
        $(".prev").removeClass("active");
        $(".next").removeClass("active");
    };
    
    function getActive(){
        return $("#pag-right li.active a").attr("ident");
    };
    
    function getPages(){
        return Math.ceil(pub_rows/page_size);
    };

    function appendPrevButton(){
        var li = $("<li class=\"prev first\"></li>");
        var active_id = parseInt(getActive());
        var prev = active_id > page_start ? active_id-1 : page_start;
        var link = $("<a></a>").attr("ident",prev).css({"cursor": "pointer"}).appendTo(li);
        li.insertBefore("#pag-right li:first");
    };

    function appendNextButton(){
        var li = $("<li class=\"next first\"></li>");
        var active_id = parseInt(getActive());
        var pages = getPages();
        var next = active_id == pages ? pages : active_id + 1;
        var link = $("<a></a>").attr("ident",next).css({"cursor": "pointer"}).appendTo(li);
        li.insertAfter("#pag-right li:last");
    };

    function updatePrevButton(){
        var active_id = parseInt(getActive());
        var prev = active_id > page_start ? active_id-1 : page_start;
        $(".prev a").attr("ident", prev);
    };

    function updateNextButton(){
        var active_id = parseInt(getActive());
        var pages = getPages();
        var next = active_id == pages ? pages : active_id + 1;
        $(".next a").attr("ident", next);
    };
    
    function hideButtons(){
        var active_id = getActive();
        var pages = getPages();
        if(active_id == page_start){
            $(".prev").css({"visibility":"hidden"});
        }
        else if(active_id == pages){
            $(".next").css({"visibility":"hidden"});
        }else{
            $(".prev").css({"visibility":"visible"});
            $(".next").css({"visibility":"visible"});
        };
    };
    
    function showPage(){
        var active_id = parseInt(getActive());
        var pages = getPages();
        var start = active_id == page_start ? 0 : (active_id-1) * page_size;
        var end = (active_id * page_size) - 1;
        $(".pub-row").show();
        $(".pub-row:lt(" + parseInt(start) + ")").hide();
        $(".pub-row:gt(" +parseInt(end)+ ")").hide();
        updatePrevButton();
        updateNextButton();
    };

    generatePaginator();
    
    $("#pag-right li a").click(function(){
        var ident = $(this).attr("ident");
        setActive(ident);
        hideButtons();
        showPage();
    });
});
