/**
 * Created by kde713 on 2017. 6. 5..
 */

const NOTICE_API_ENDPOINT = "https://o33sjgoqh2.execute-api.ap-northeast-2.amazonaws.com/prod/Temp-Crawler0";
const NOTICE_READ_URL = "https://www.kookmin.ac.kr/ETC/office/bachelor.htm?idx=";

var current_page = 0;
var ajax_flag = true;
var search_flag = "";

function gotoTop() {
    $("html, body").animate({scrollTop: 0}, "slow");
}

function openNotice(notice_id) {
    window.open(NOTICE_READ_URL + notice_id);
}

function clearNotice() {
    $("#notice-list").html("");
}

function loadNotice(page_no, query = '') {
    $.ajax({
        type: "GET",
        url: `${NOTICE_API_ENDPOINT}?page_no=${page_no}&query=${query}`,
        cache: false,
        success: function (data) {
            console.log("success");
            let notice_list = data.notices;
            if (notice_list.length < 1) {
                $("#message-box").text("더 이상 불러올 수 있는 게시물이 없습니다.");
                $("#message-box").show();
                $("#message-box").fadeOut(2500);
            } else {
                for (var notice of notice_list) {
                    $("#notice-list").append(`<div class="card" onclick="openNotice(${notice.link})"> <div class="container"><h3 class="notice-title">${notice.title}</h3> <p class="notice-subtitle">${notice.date} | ${notice.author}</p> </div> </div> <div class="clear"></div>`);
                }
                current_page += 1;
            }
        },
        error: function (e) {
            $("#message-box").text("서버 오류가 발생하였습니다.");
            $("#message-box").show();
            $("#message-box").fadeOut(2500);
        },
        complete: function () {
            ajax_flag = false;
            $("#loader").hide();
        }
    });
}

function searchAction() {
    let query = $("#search-form").val();
    if (query) {
        clearNotice();
        search_flag = query;
        current_page = 0;
        $("#search-cancel").show();
        ajax_flag = true;
        $("#loader").show();
        setTimeout(function () {
            loadNotice(current_page, search_flag);
        }, 1000);
    } else {
        alert("검색어를 입력해주세요!");
    }
}

function clearSearch() {
    $("#search-cancel").hide();
    $("#search-form").val("");
    search_flag = "";
    current_page = 0;
    clearNotice();
    ajax_flag = true;
    $("#loader").show();
    setTimeout(function () {
        loadNotice(current_page);
    }, 1000);
}

$(function () {
    $("#message-box").hide();
    $("#search-cancel").hide();
    setTimeout(function () {
        loadNotice(current_page);
    }, 1000);

    $(window).scroll(function () {
        if ($(window).scrollTop() == $(document).height() - $(window).height()) {
            if (!ajax_flag) {
                console.log("Scroll #" + current_page);
                ajax_flag = true;
                $("#loader").show();
                setTimeout(function () {
                    if (search_flag) loadNotice(current_page, search_flag);
                    else loadNotice(current_page);
                }, 1000);
            }
        }

        if ($(window).scrollTop() > ($(window).height() / 2)) $("#topBtn").show();
        else $("#topBtn").hide();
    });

    $("#search-form").on('keydown', function (e) {
        if (e.which == 13) {
            e.preventDefault();
            searchAction()
        }
    });
    $("#search-submit").click(searchAction);
    $("#search-cancel").click(clearSearch);

});
