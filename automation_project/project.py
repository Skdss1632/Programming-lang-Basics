from utility_functions import *


def schedule_task_at_specific_time():
    # click_mouse_position()
    click_on_wl_or_avalible_btn()
    click_book_now_inside_select_train(book_now_img_path=get_image_path("book_now_image"))
    # if want to perform any action inside pass details count the presses from gender
    input_passenger_names()
    input_passenger_phn_no()
    if get_ticket_availability_status("is_ticket_available"):
        click_book_only_if_confirm_berth_alloted()
    if get_otp_and_payment_options("is_payment_with_upi"):
        scroll_until_element_visible_not_visible(img_path=get_image_path("pay_through_bhim_upi_image"))
        click_pay_with_upi()
    click_continue_btn_inside_pass_details()
    # here page start buffering
    wait_for_element(image_path=get_image_path("review_journey_image"))
    # if ad blocker extension installed on browser no need to sleep here for 1 sec
    # py.sleep(1)
    click_captcha_fld(is_ad_blocker_enabled=True)
    # press enter manually after filling captcha
    wait_for_element(image_path=get_image_path("payment_yellow_image"))
    # if ad blocker extension installed on browser no need to sleep here for 1 sec
    # py.sleep(1)
    if get_otp_and_payment_options("is_payment_with_upi"):
        click_bhim_upi_ssd()
        click_pay_using_bhim_paytm_txt()
        click_pay_n_book(no_of_press=4)
    else:
        # if want to pay with wallet verify you have created wallet in acc and have required amt in it
        click_irctc_e_wallet(img_path=get_image_path("irctc_e_wallet_image"))
        is_irctc_wallet_clicked()
        click_pay_n_book(no_of_press=10)
        # if want to pay with wallet need to click on otp fld otherwise not, if want to pay with upi just scan qr and pay
        click_otp_fld(otp_fld_img_path=get_image_path("otp_fld_image"))
    if get_otp_and_payment_options("is_read_and_write_otp_from_sms"):
        read_n_write_otp_from_kde_sms()
    else:
        read_and_write_otp_from_mail()


# schedule_task_at_specific_time()


if get_coach_booking_preferences("is_ac_3_tier") or get_coach_booking_preferences("is_ac_tier_3_economy"):
    time = "10:00:00"
else:
    time = "11:00:00"
schedule.every().day.at(time).do(schedule_task_at_specific_time)
while True:
    schedule.run_pending()
