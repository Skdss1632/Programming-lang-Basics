from Programming_Lang_Basics.automation_project.utility_functions import *  # Custom utility functions


def input_details():
    """Automates the process of inputting details on the IRCTC page.
    if you want to book ticket in another train take that train ss and pass the img path train_name_image"""
    open_chrome_browser_with_irctc_page()
    click_login_btn()
    py.sleep(3)
    # # validate login popup open or not
    # otp_fld_location = py.locateCenterOnScreen(image=, confidence=0.80, minSearchTime=10)

    username_field_image = get_image_path("username_field_image")
    password_field_image = get_image_path("password_field_image")
    username = get_credentials("username")
    password = get_credentials("password")
    input_irctc_account(username=username, password=password, username_image_path=username_field_image,
                        password_image_path=password_field_image)

    source_station = get_booking_details("source_station")
    destination_station = get_booking_details("destination_station")
    input_source_n_destination_station(source_station=source_station, destination=destination_station)

    select_ticket_type_from_dropdown()

    tatkal_book_date = get_booking_details("travel_date")
    input_travel_date(tatkal_book_date=tatkal_book_date)

    reset_filter_txt_img_path = get_image_path("reset_filter_image")
    py.locateCenterOnScreen(image=reset_filter_txt_img_path, confidence=0.90, minSearchTime=60)
    py.sleep(1)

    train_name_img_path = get_image_path("train_name_image")
    scroll_until_element_visible_not_visible(img_path=train_name_img_path)
    py.sleep(0.2)
    # py.sleep(8)


def schedule_task_at_specific_time():
    # py.sleep(2)
    click_on_coach_on_selected_train()

    click_on_wl_or_avalible_btn()

    book_now_img_path = get_image_path("book_now_image")
    scroll_until_element_visible_not_visible(book_now_img_path)
    click_book_now_inside_select_train(book_now_img_path=book_now_img_path)

    passenger_detail_img_path = get_image_path("passenger_details_image")
    passenger_names = get_booking_details("passenger_names")
    py.sleep(0.3)
    select_passenger_from_master_lst(passenger_name=passenger_names,
                                     passenger_details_img_path=passenger_detail_img_path)

    if get_booking_details("is_tatkal") or get_booking_details("is_premium_tatkal"):
        click_book_only_if_confirm_berth_alloted(get_image_path("book_only_if_get_confirm_berth"))

    continue_btn_img_path = get_image_path("continue_button_image")
    scroll_until_element_visible_not_visible(img_path=continue_btn_img_path)
    click_continue_btn_inside_passenger_details(continue_btn_img_path=continue_btn_img_path)

    view_cancellation_img_path = get_image_path("review_journey_image")
    py.locateCenterOnScreen(image=view_cancellation_img_path, confidence=0.90, minSearchTime=60)
    py.scroll(-2.5)
    py.sleep(0.3)
    click_captcha_fld()

    payment_yellow_img_path = get_image_path("payment_yellow_image")
    py.locateCenterOnScreen(image=payment_yellow_img_path, confidence=0.90, minSearchTime=60)
    py.sleep(1)

    irctc_e_wallet_img_path = get_image_path("irctc_e_wallet_image")
    click_irctc_e_wallet(img_path=irctc_e_wallet_img_path)

    # verify irctc e wallet btn is clicked
    an_amt_of_10_applicable_txt_image = get_image_path("an_amt_of_10_applicable_txt_image")
    py.locateCenterOnScreen(image=an_amt_of_10_applicable_txt_image, confidence=0.90, minSearchTime=60)

    pay_n_book_img_path = get_image_path("pay_n_book_image")
    scroll_until_element_visible_not_visible(pay_n_book_img_path)
    click_pay_n_book(img_path=pay_n_book_img_path)

    confirm_btn_img_path = get_image_path("confirm_btn_image")
    otp_fld_img_path = get_image_path("otp_fld_image")
    click_confirm_btn_inside_otp(img_path=confirm_btn_img_path, otp_fld_img_path=otp_fld_img_path)


# Execute the input details function
# input_details()
schedule_task_at_specific_time()

# Schedule the task to run at 07:25 AM every day
# schedule.every().day.at("08:40:40").do(schedule_task_at_specific_time)
#
# while True:
#     schedule.run_pending()
