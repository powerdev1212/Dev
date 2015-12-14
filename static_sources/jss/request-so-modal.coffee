
expert_pk = null

window.runRequestSOModal = (pk)->
    expert_pk = pk
    min_height=0
    $('#soModal').modal().on('shown.bs.modal',
        ()->
            about_so = $('.modal-so-request').find('.about-so')
            for li in about_so.find('li')
                div = $(li).find('div')
                div = $(div)
                console.log div
                console.log div.height()
                if div.height()>min_height
                    min_height = div.height()
            h = about_so.find('h3').height()
            about_so.css('min-height', min_height+h*6+'px')
            console.log min_height
    )

window.openSoPage = ()->
    location.href = "http://hygeiais.com/so/experts/"+expert_pk
