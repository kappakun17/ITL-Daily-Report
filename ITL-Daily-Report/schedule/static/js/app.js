


document.addEventListener('DOMContentLoaded', function () {

    axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
    axios.defaults.xsrfCookieName = 'csrftoken'


    var scheduleEl = document.getElementById('calendar');
    var schedule = new FullCalendar.Calendar(scheduleEl, {

        //header bar
        contentHeight: 'auto',
        locale:'js',
        headerToolbar: {
            left: 'prev,today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay,next'
        },
        navLinks: false,
        editable: false,
        views: {
            timeGridWeek: {
                slotMinTime: '09:00:00',
                slotMaxTime: '18:00:00',
            },
            timeGridDay: {
                slotMinTime: '09:00:00',
                slotMaxTime: '18:00:00',
            },
        },
        dayCellContent: function (e) {
            e.dayNumberText = e.dayNumberText.replace('日','')
        },
        selectable: true,
        eventClick: function (info) {
            displayEvent(info.event)
            changeDetailBtn()
        },
        
        events: function (info, successCallback, failureCallback) {
            axios
               .post('/dashboard/user/schedule/get/list', {
                    start_date: info.start.valueOf(),
                   end_date: info.end.valueOf(),
                })
                .then((response) => {
                    schedule.removeAllEvents();
                    successCallback(response.data);
                    changeListData(response.data, info.start)
                })
                .catch((error) => {
                    alert(error)
                })
        },
 

    });

    

    schedule.render();

});

document.getElementById('my-next-button')

function changeListData(data, startMonth) {
    scheduleTable = document.getElementById('schedule-table')
    scheduleTbody = scheduleTable.tBodies[0];
    console.log(startMonth)


    tbody_t = ``
    for (let i = 0; i < data.length; i++) {
        date = new Date(data[i].start)

        var dayOfWeek = date.getDay()
        var dayOfWeekStr = ['日','月', '火', '水', '木', '金', '土'][dayOfWeek]

        let is_dialy_btn = ''
        console.log(data[i])
        if (data[i].is_dialy) {
            is_dialy_btn = '<i class="bi bi-check-circle-fill text-success h6"></i>'
        }
        
        tbody_t += `
            <tr>
                <th scope="row">${formatDate(date, 'MM/dd')}<span style='font-size:14px'>(${dayOfWeekStr})</span></th>
                <td>${data[i].title}</td>
                <td><a href="/dashboard/user/dialy/edit/${data[i].id}">日報はこちら</a></td>
                <td class="">${is_dialy_btn}</td>


            </tr>
        `

        
        if (dayOfWeekStr == '金') {
            tbody_t += `<td colspan='4' class='text-danger text-center fw-normal'>休日</td>`

        }
        
    }
    console.log(tbody_t)

    scheduleTbody.innerHTML = tbody_t
    
}

function displayEvent(event) {

    if (document.getElementById('diary-btn')) {
        var diaryBtn = document.getElementById('diary-btn')
        diaryBtn.remove()
    }

    dialyBtnText = ''
    dialy_btn_color = ''
    if (event.extendedProps.is_dialy) {
        dialyBtnText = '日報を見る'
        dialy_btn_color = 'btn-warning'
    }
    else {
        dialyBtnText = '日報を書く'
        dialy_btn_color = 'btn-success'
    }

    var disDiv = document.getElementById('display-div')
    //var disForm = document.getElementById('form-detail-id')
    var disTitle = document.getElementById('display-title')
    var disDes = document.getElementById('display-description')
    var disDate = document.getElementById('display-date')
    //var disTime = document.getElementById('display-time')
    var disStaff = document.getElementById('display-staff-memo')
    var disTraineer = document.getElementById('display-traineer-memo')
    //var disDetailHiddenId = document.getElementById('detail-hidden-id')
    var dialyBtn = document.createElement('button')

    dialyBtn.classList.add('btn')
    
    dialyBtn.classList.add(dialy_btn_color)
    dialyBtn.innerHTML = dialyBtnText
    dialyBtn.setAttribute('id', 'diary-btn')

    dialyBtn.addEventListener('click', function () {
        if (dialyBtn.innerHTML == '日報を見る') {
            location.replace(`/dashboard/user/dialy/detail/${event.id}`);
        }else{
            location.replace(`/dashboard/user/dialy/edit/${event.id}`);

        }
    })

    disDiv.appendChild(dialyBtn)

    disDate.innerHTML = '<i class="bi bi-calendar"></i> ' + formatDate(event.start, 'yyyy/MM/dd') + ' ' + formatDate(event.start, 'HH:mm') + " - " + formatDate(event.end, 'HH:mm')
    disTitle.innerHTML ='<i class="bi bi-bookmark"></i> '+ event.title
    disDes.innerHTML = '<i class="bi bi-book"></i> ' + event.extendedProps.description
    if (event.extendedProps.staff_memo) disStaff.innerHTML = '<i class="bi bi-brush"></i> ' + event.extendedProps.staff_memo
    else disStaff.innerHTML = ''
    if (event.extendedProps.traineer_mem) disTraineer.innerHTML = '<i class="bi bi-brush"></i> ' + event.extendedProps.traineer_memo
    else disTraineer.innerHTML = ''


}

function formatDate(date, format) {
    format = format.replace(/yyyy/g, date.getFullYear());
    format = format.replace(/MM/g, ('0' + (date.getMonth() + 1)).slice(-2));
    format = format.replace(/dd/g, ('0' + date.getDate()).slice(-2));
    format = format.replace(/HH/g, ('0' + date.getHours()).slice(-2));
    format = format.replace(/mm/g, ('0' + date.getMinutes()).slice(-2));
    format = format.replace(/ss/g, ('0' + date.getSeconds()).slice(-2));
    format = format.replace(/SSS/g, ('00' + date.getMilliseconds()).slice(-3));
    return format;
};

var detailBar = document.getElementById('detail-bar')
var listBar = document.getElementById('plan-view-bar')

var displayDiv = document.getElementById('display-div')
var displayList = document.getElementById('display-list')

function changeDetailBtn() {
    listBar.classList.remove('active')
    detailBar.classList.add('active')
    displayDiv.classList.remove('d-none')
    displayList.classList.add('d-none')
}

detailBar.addEventListener('click', function () {
    listBar.classList.remove('active')
    detailBar.classList.add('active')
    displayDiv.classList.remove('d-none')
    displayList.classList.add('d-none')
})

listBar.addEventListener('click', function () {
    detailBar.classList.remove('active')
    listBar.classList.add('active')
    displayDiv.classList.add('d-none')
    displayList.classList.remove('d-none')
})


