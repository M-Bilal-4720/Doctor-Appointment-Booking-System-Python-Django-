from django.shortcuts import render,redirect,get_object_or_404,reverse
from .models import  *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from datetime import date ,timedelta, datetime
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from django.db.models import Sum
from django.core.paginator import Paginator

# Create your views here.
def home(request):
   reviews = Review.objects.select_related('doctor__user', 'patient__user','doctor__specialization').all()
   return render (request,'index.html',{'reviews':reviews})
def tc(request):
   return render (request,'term-condition.html')
def contact(request):
   if request.method=='POST':
      name=request.POST.get('name')
      email=request.POST.get('email')
      message=request.POST.get('message')
      add=Contact.objects.create(name=name,email=email,message=message)
      add.save()
      messages.success(request,'Message send successfully')
      return redirect('contact')
   return render (request,'contact-us.html')
def about(request):
   return render (request,'about-us.html')
def search(request):
   #doctors = Doctor.objects.select_related('user', 'specialization').filter(status='active')
   doctors = Doctor.objects.filter(status='active')
   total_doctors=doctors.count()
   specialty=Specialization.objects.all()
   return render (request,'search.html',{'total_doctors':total_doctors,'specialty':specialty,'doctors':doctors})
def search_doctor(request,specialty_id):
   #doctors = Doctor.objects.select_related('user', 'specialization').filter(status='active')
   specialty=Specialization.objects.all()
   doctors = Doctor.objects.filter(status='active',specialization=specialty_id)
   total_doctors=doctors.count()
   return render (request,'search.html',{'total_doctors':total_doctors,'specialty':specialty,'doctors':doctors})
def view_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    id = doctor.user
    clinic = get_object_or_404(Clinic, doctor=id)
    service = get_object_or_404(Services, doctor=id)
    degree = get_object_or_404(Degrees, doctor=id)
    experience = get_object_or_404(Experience, doctor=id)
    award = get_object_or_404(Award, doctor=id)
    sechdules = DoctorSchedule.objects.filter(doctor=doctor_id)
    special = doctor.specialization
    reviews = Review.objects.select_related('doctor__user', 'patient__user').all()
    context={'reviews':reviews,'sechdules':sechdules,'experience':experience,'award':award,'clinic':clinic,'degree':degree,'special':special,'service':service,'doctors':doctor}
    return render (request,'doctor-profile.html',context)
def booking(request,doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    selected_date = datetime.now().date()  # You can replace this with the selected date from the user
    days = []
    for i in range(7):  # Show schedule for the next 7 days from the selected date
        date = selected_date + timedelta(days=i)
        day_of_week = date.strftime('%A')
        schedule = DoctorSchedule.objects.filter(doctor=doctor, day_of_week=day_of_week)
        time_slots = []
        for slot in schedule:
            time_slots.append({
                'start_time': slot.start_time,
                'end_time': slot.end_time,
            })
        days.append({
            'date': date,
            'day_name': day_of_week,
            'time_slots': time_slots,
        })
    
    return render(request, 'booking.html', {'doctor': doctor, 'days': days, 'selected_date': selected_date})

def book_appointment(request):
    if request.method == 'POST':
        appt_date_str = request.POST.get('selected_date')
        appt_time_str = request.POST.get('selected_time')
        doctor_id = request.POST.get('doctor_id')
        doctor = Doctor.objects.get(id=doctor_id)
        appt_time = datetime.strptime(appt_time_str, '%H:%M').time()
        appt_date = datetime.strptime(appt_date_str, '%B %d, %Y').date()
        # Check if the user is logged in as a patient
       
        if request.user.is_authenticated and request.user.is_patient:
            patient = request.user.patient
            booking_date = datetime.now().date()
            existing_appointment = Appointment.objects.filter(patient=patient, appt_date=appt_date, doctor=doctor).first()
            if existing_appointment:
                messages.error(request,'You have already booked an appointment with the same doctor on this date.')
                return redirect('booking',doctor_id=doctor_id)
            
            book = Appointment.objects.create(doctor=doctor, booking_date=booking_date, patient=patient, appt_date=appt_date, appt_time=appt_time)
            book.save()
          
            # Pass the appointment details to the template
            doctor_name = doctor.user.get_full_name()
            formatted_appt_date = appt_date.strftime('%d %b %Y')
            formatted_appt_time = appt_time.strftime('%I:%M %p')

            # Pass the appointment details to the template
            context = {
                'doctor_name': doctor_name,
                'appt_date_time': f"{formatted_appt_date} {formatted_appt_time}",
            }

            return render(request, 'success-page.html', context)
        else:
            # If the user is not logged in as a patient, handle the error or redirect to the login page
            return redirect('patient_login')  # Replace 'login' with the URL name of your login page
    else:
        return redirect('book_appointment')


#Admin views
@login_required(login_url='/dash_access')
def admin_panel(request):
  if request.user.is_authenticated and request.user.is_admin:  
    c_user=request.user
    subadmin=Subadmin.objects.get(user=request.user)
    patients = User.objects.filter(is_patient=True).select_related('patient')
    doctors = Doctor.objects.select_related('user', 'specialization').all()
    total_patients = User.objects.filter(is_patient=True).count()
    total_doctors = User.objects.filter(is_doctor=True).count()
    total_appointment=Appointment.objects.count()
    total_revenue = Payment.objects.aggregate(total=Sum('amount'))['total']
    per_patient=total_patients/100
    per_appointment=total_appointment/100
    per_doctor=total_doctors/100
    appointments = Appointment.objects.select_related('patient', 'doctor__user', 'doctor__specialization').all()
    context = {'appointments': appointments,'subadmin':subadmin,'total_revenue':total_revenue,'per_patient':per_patient,'per_doctor':per_doctor,'per_appointment':per_appointment,'total_appointment':total_appointment,'total_patients':total_patients,'total_doctors':total_doctors,'patients': patients,'c_user':c_user,'doctors':doctors}
    return render(request,'admin/index_admin.html',context)
  else:
     return redirect('dash_access')
def dash_access(request):
   if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_admin:
            login(request, user)
            return redirect('admin_panel')
        else:
            messages.error(request,'Wrong Caridentials')
            return redirect('dash_access')
   return render(request,'admin/dash_login.html')
@login_required(login_url='/dash_access')
def patient_list(request):
  if request.user.is_authenticated and request.user.is_admin:  
    patients = User.objects.filter(is_patient=True).select_related('patient')
    c_user=request.user
    subadmin=Subadmin.objects.get(user=request.user)
    context = {'patients': patients,'c_user':c_user,'subadmin':subadmin}
    return render(request,'admin/patient-list.html', context)
  else:
     return redirect('dash_access')
@login_required(login_url='/dash_access')
def doctor_list(request):
  if request.user.is_authenticated and request.user.is_admin:  
    doctors = Doctor.objects.select_related('user', 'specialization').all()
    c_user=request.user
    subadmin=Subadmin.objects.get(user=request.user)
    context = {'c_user':c_user,'subadmin':subadmin,'doctors': doctors}
    return render(request,'admin/doctor-list.html',context)
  else:
     return redirect('dash_access')
@login_required(login_url='/dash_access')
def update_doctor_status(request):
  if request.user.is_authenticated and request.user.is_admin:  
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        status = request.POST.get('status')

        try:
            doctor = Doctor.objects.get(id=doctor_id)
            doctor.status = status
            doctor.save()
            return JsonResponse({'status': 'success'})
        except Doctor.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Doctor not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
  else:
     return redirect('dash_access')
@login_required(login_url='/dash_access')
def admin_appointment(request):
 if request.user.is_authenticated and request.user.is_admin:  
    appointments = Appointment.objects.select_related('patient', 'doctor__user', 'doctor__specialization').all()
    c_user=request.user
    subadmin=Subadmin.objects.get(user=request.user)
    context = {'c_user':c_user,'subadmin':subadmin, 'appointments': appointments
    }
    return render(request,'admin/appointment-list.html',context)
 else:
    return redirect('dash_access')
@login_required(login_url='/dash_access')
def admin_appointment_status(request):
  if request.user.is_authenticated and request.user.is_admin:
    if request.method == 'POST':
        appoint_id = request.POST.get('appoint_id')
        status = request.POST.get('status')

        try:
            appointment = get_object_or_404(Appointment, id=appoint_id)
            appointment.status = status
            appointment.save()
            return JsonResponse({'status': 'success'})
        except Appointment.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Appointment not found'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
  else:
     return redirect('dash_access')
@login_required(login_url='/dash_access')
def admin_specialities(request):
 if request.user.is_authenticated and request.user.is_admin:  
   specialtys=Specialization.objects.all()
   c_user=request.user
   subadmin=Subadmin.objects.get(user=request.user)
   context = {'c_user':c_user,'subadmin':subadmin,'specialtys':specialtys}
   return render(request,'admin/specialities.html',context)
 else:
    return redirect('dash_access')
@login_required(login_url='/dash_access')
def update_specialty(request, specialty_id):
  if request.user.is_authenticated and request.user.is_admin:
    specialtys = Specialization.objects.get(id=specialty_id)
    if request.method == 'POST':
        specialty = Specialization.objects.get(id=specialty_id)
        name = request.POST.get('name')
        special_image = request.FILES.get('special_image')
        specialty.name = name
        if special_image:
            specialty.special_image = special_image
            specialty.save()
            messages.success(request,'Specialization update successfully')
        return redirect('admin_specialities')

    c_user=request.user
    subadmin=Subadmin.objects.get(user=request.user)
    context = {'c_user':c_user,'subadmin':subadmin,'specialty':specialtys}
    return render(request,'admin/edit-specialities.html',context)
  else:
     return redirect('dash_access')
@login_required(login_url='/dash_access')
def delete_specialty(request, specialty_id):
   if request.user.is_authenticated and request.user.is_admin: 
    specialty = get_object_or_404(Specialization, id=specialty_id)
    specialty.delete()
    messages.success(request,'Specialitie Delete Successfully')
    return redirect('admin_specialities')
   else:
      return redirect('dash_access')
@login_required(login_url='/dash_access')
def add_specialities(request):
  if request.user.is_authenticated and request.user.is_admin:
   if request.method=="POST":
       name = request.POST.get('name','')
       special_image = request.FILES.get('special_image','')
       try:
           special_name=Specialization.objects.get(name=name)
           messages.error(request,'Speciality already exist')
           return redirect('admin_specialities')
       except Specialization.DoesNotExist:
            add=Specialization.objects.create(name=name,special_image=special_image)
            add.save()
            messages.success(request,'Specialities Add Successfully')
            return redirect('admin_specialities')
   return redirect ('admin_specialities')
  else:
     return redirect('dash_access')    
@login_required(login_url='/dash_access')
def admin_reviews(request):
 if request.user.is_authenticated and request.user.is_admin:  
    reviews = Review.objects.select_related('doctor__user', 'patient__user').all()
    c_user=request.user
    subadmin=Subadmin.objects.get(user=request.user)
    context = {'c_user':c_user,'subadmin':subadmin,'reviews':reviews}
    return render(request,'admin/reviews.html',context)
 else:
    return redirect('dash_access')
@login_required(login_url='/dash_access')
def delete_review(request,review_id):
  if request.user.is_authenticated and request.user.is_admin: 
   payments = Payment.objects.get(id=review_id)
   payments.delete()
   messages.success(request,'Review Successfully Delete')
   return redirect('admin_reviews')
  else:
     return redirect('dash_access')
@login_required(login_url='/dash_access')
def admin_profile(request):
  if request.user.is_authenticated and request.user.is_admin:  
    user=request.user
    try:
      subadmin = Subadmin.objects.get(user=request.user)
      if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        subadmin = Subadmin.objects.get(user=request.user)
        subadmin.admin_image = request.FILES.get('admin_image', subadmin.admin_image)
        subadmin.date_birth = request.POST.get('date_birth', subadmin.date_birth)
        subadmin.blood_group = request.POST.get('blood_group', subadmin.blood_group)
        subadmin.gender = request.POST.get('gender', subadmin.gender)
        subadmin.phone = request.POST.get('phone', subadmin.phone)
        subadmin.address = request.POST.get('address', subadmin.address)
        subadmin.city = request.POST.get('city', subadmin.city)
        subadmin.state = request.POST.get('state', subadmin.state)
        subadmin.postal_code = request.POST.get('postal_code', subadmin.postal_code)
        subadmin.country = request.POST.get('country', subadmin.country)
        subadmin.save()
        return redirect('admin_profile')
    except Subadmin.DoesNotExist:
        messages.error(request, 'Please complete your')
        return redirect('profile_create')  # Replace 'profile' with the URL name of the profile page
    context={'user':user,'subadmin':subadmin}
    return render(request,'admin/profile.html',context)
  else:
     return redirect('dash_access')
@login_required(login_url='/dash_access')
def profile_create(request):
  if request.user.is_authenticated and request.user.is_admin:  
    if request.method=='POST':
           admin_image = request.FILES.get('admin_image', '')
           date_birth = request.POST.get('date_birth', '')
           blood_group = request.POST.get('blood_group','')
           gender = request.POST.get('gender', '')
           phone = request.POST.get('phone', '')
           address = request.POST.get('address', '')
           city = request.POST.get('city', '')
           state = request.POST.get('state', '')
           postal_code = request.POST.get('postal_code','')
           country = request.POST.get('country', )
           addadmin=Subadmin.objects.create(user=request.user,city=city,state=state,country=country,postal_code=postal_code,address=address,admin_image=admin_image,date_birth=date_birth,blood_group=blood_group,gender=gender,phone=phone)
           addadmin.save()
           messages.success(request, 'Profile update successfully')
           return redirect('admin_profile')
    return render(request,'admin/profile_create.html')
  return redirect(dash_access)
@login_required(login_url='/dash_access')
def ad_password_ch(request):
  if request.user.is_authenticated and request.user.is_admin:
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        user = request.user

        # Check if the old password is correct
        if not user.check_password(old_password):
            messages.error(request, 'Incorrect old password')
            return redirect('doc_password_ch')

        # Check if the new password and confirm password match
        if new_password != confirm_password:
            messages.error(request, 'New password and confirm password do not match')
            return redirect('doc_password_ch')

        # Set the new password and save the user
        user.set_password(new_password)
        user.save()

        messages.success(request, 'Password changed successfully')
        return redirect('admin_panel')
    return redirect('admin_panel')
  else:
     return redirect('dash_access')
@login_required(login_url='/dash_access')
def ad_logout(request):
  if request.user.is_authenticated and request.user.is_admin:
   logout(request)
   return redirect ('dash_access')
  else:
     return redirect('dash_access')
@login_required(login_url='/dash_access')
def transaction_list(request):
   if request.user.is_authenticated and request.user.is_admin:
    payments = Payment.objects.select_related('patient', 'doctor__user', 'doctor__specialization').all()
    c_user=request.user
    subadmin=Subadmin.objects.get(user=request.user)
    context = {'c_user':c_user,'subadmin':subadmin,'payments':payments}
    return render(request,'admin/transactions-list.html',context)
   else:
      return redirect('dash_access')
@login_required(login_url='/dash_access')
def delete_transaction(request ,payment_id):
  if request.user.is_authenticated and request.user.is_admin:
    payment = Payment.objects.get(id=payment_id)
    payment.delete()
    return redirect('transaction_list')
  else:
     return redirect('dash_access')
   #doctor views
def admin_forgot_password(request):
    if request.method=='POST':
        email = request.POST.get('email')
        last_name = request.POST.get('last_name')

        # Retrieve the user with the provided email and last name
        try:
            user = User.objects.get(email=email, last_name=last_name)
        except User.DoesNotExist:
            messages.error(request, 'User with the provided email and last name does not exist')
            return redirect('admin_forgot_password')

        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('con_password')

        # Check if the new password and confirm password match
        if new_password != confirm_password:
            messages.error(request, 'New password and confirm password do not match')
            return redirect('admin_forgot_password')

        # Set the new password and save the user
        user.set_password(new_password)
        user.save()

        messages.success(request, 'Password reset successfully')
        return redirect('dash_access')
    return render(request,'admin/forgot-password.html')
def contacts(request):
   if request.user.is_authenticated and request.user.is_admin:
     contact=Contact.objects.all()
     return render(request,'admin/contact.html',{'contact':contact})
   else:
    return redirect('dash_access')
def delete_contact(request,contact_id):
   if request.user.is_authenticated and request.user.is_admin:
      contact=Contact.objects.get(id=contact_id)
      if contact:
        contact.delete()
        messages.success(request,'Contact Deleted')
        return redirect('contacts')
      return render(request,'admin/contact.html')
   else:
    return redirect('dash_access')
#Doctor Views

def profile_add_doc4(request):
  if request.user.is_authenticated and request.user.is_doctor:
    if request.method=="POST":
        #Award inputs
        doc=request.user
        doctor_id=doc.id
        doctor_id=doctor_id
        awards = request.POST.get('awards','')
        award_years = request.POST.get('award_year','')
        award_instance = Award(doctor_id=doctor_id, awards=awards, award_year=award_years)
        award_instance.save()
        return redirect('doc_panel')
    else:
        return render(request,'add_profile_doc4.html')
  else:
     return redirect('doctor_login')

def profile_add_doc3(request):
  if request.user.is_authenticated and request.user.is_doctor:
    if request.method=='POST':
        degrees = request.POST.get('degree','')
        institutes = request.POST.get('institute','')
        years = request.POST.get('year','')
        #Experiance
        hospital_name = request.POST.get('hospital_name','')
        designation = request.POST.get('designation','')
        start_dates = request.POST.get('start_date','')
        end_dates = request.POST.get('end_date','')
        doc=request.user
        doctor_id=doc.id
        doctor_id=doctor_id
        Exper=Experience( doctor_id=doctor_id, hospital_name=hospital_name,designation=designation,start_date=start_dates, end_date=end_dates )
        Exper.save()
        education=Degrees( doctor_id=doctor_id, degree=degrees,institute=institutes, year=years )
        education.save()
        return redirect("profile_add_doc4")
    else:
        return render(request,'add_profile_doc3.html')
  else:
     return redirect('doctor_login')

def profile_add_doc2(request):
  if request.user.is_authenticated and request.user.is_doctor:
    doc=request.user
    doctor_id=doc.id
    doctor_id=doctor_id
    if request.method == 'POST':
        clinic_name = request.POST.get('clinic_name','')
        clinic_image = request.FILES.get('clinic_image','')
        clinic_address = request.POST.get('clinic_address','')
        #Services and Specializations
        services = request.POST.getlist('service','')
   
        practic=Clinic( doctor_id=doctor_id, clinic_name=clinic_name,clinic_address=clinic_address, clinic_image=clinic_image )
      
        practic.save()
        for service in services:
            service_instance = Services(doctor_id=doctor_id, service=service)
            service_instance.save()
        return redirect('profile_add_doc3')
    
    return render(request,'add_profile_doc2.html')
  else:
     return redirect('doctor_login')

def profile_add_doc(request):
  if request.user.is_authenticated and request.user.is_doctor:
    doc=request.user
    doctor_id=doc.id
    specialtys=Specialization.objects.all()
    if request.method=='POST':
        doctor_id=request.user
        # Update the doctor instance with the submitted form data
        gender = request.POST.get('gender', '')
        phone = request.POST.get('phone', '')
        date_birth = request.POST.get('date_birth', '')
        biography = request.POST.get('biography', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        specialization_id = request.POST.get('specialization', '')
        specialization = Specialization.objects.get(id=specialization_id)
        country = request.POST.get('country', '')
        state = request.POST.get('state', '')
        postal_code = request.POST.get('postal_code', '')
        price = request.POST.get('price', '')  # Only used if pricing_type is 'free'
        doc_image = request.FILES.get('doc_image', '')  # Assuming the form has a file input named 'doc_image'
        profile=Doctor.objects.create(user=doctor_id,specialization=specialization,price=price,gender=gender,phone=phone,date_birth=date_birth,biography=biography,address=address,city=city,country=country,state=state,postal_code=postal_code,doc_image=doc_image)
        profile.save()
        return redirect('profile_add_doc2')
    context={'specialtys':specialtys}
    return render(request,'add_profile_doc.html',context)
  else:
      return redirect('doctor_id')
def doctor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_doctor:
            login(request, user)
            try:
                doctor = Doctor.objects.get(user=user)
                # Redirect to profile page if doctor profile exists
                messages.success(request, 'Login successfully')
                return redirect('doc_panel')
            except Doctor.DoesNotExist:
                messages.error(request, 'Please complete your profile')
                # Redirect to add profile page if patient profile doesn't exist
                return redirect('profile_add_doc')
            
        else:
            messages.error(request,'Ivalide cordentials')
            return redirect('doctor_login')
    return render (request,'doc_login.html')
def doctor_register(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            try:
                exist=User.objects.filter(username=username)
                messages.error(request,'Username Already Exisit')
                return redirect('doctor_register')
            except User.DoesNotExist:
                 user = User.objects.create_user(is_doctor= True, username=username,password=password,email=email,first_name=first_name,last_name=last_name,)
                 user.save()
                 login(request, user)
                 messages.success(request,'Your Register Successfully')
                 return redirect('profile_add_doc')
    return render (request,'doctor-register.html')

def doc_panel(request):
  if request.user.is_authenticated and request.user.is_doctor:
   doct=request.user
   user_id=request.user.id
   doctor_id = request.user.doctor.id
   doctor=Doctor.objects.get(user_id=user_id)
   special = doctor.specialization
   service = get_object_or_404(Services, doctor=doctor_id)
   degree = get_object_or_404(Degrees, doctor=doctor_id)
   current_date = date.today()
   appointments_with_details = Appointment.objects.filter(doctor_id=doctor_id).select_related('patient__user')
   appointments_todays = Appointment.objects.filter(doctor_id=doctor_id, appt_date=current_date).select_related('patient__user')
   appointments_today = Appointment.objects.filter(doctor_id=doctor_id, appt_date=current_date).count()
   total = Appointment.objects.filter(doctor_id=doctor_id).count()
   pr_total=total/100
   current_dates = timezone.now()
   year = current_dates.year
   month = current_dates.month
   appointments = Appointment.objects.filter(doctor=doctor, appt_date__year=year, appt_date__month=month)
   appointment_count=appointments.count()
   special = doctor.specialization
   context={'degree':degree,'service':service,'special':special,'doct':doct,'appointment_count':appointment_count,'pr_total':pr_total,'total':total,'appointments_todays':appointments_todays,'current_date':current_date,'appointments_today':appointments_today,'doctor':doctor,'appointments_with_details':appointments_with_details}
   return render(request,'doctor-dashboard.html',context)
  else:
      return redirect('doctor_login')

def doc_profile(request):
  if request.user.is_authenticated and request.user.is_doctor:
    doctor_id=request.user.id
    serv=Services.objects.get(doctor_id=doctor_id)
    deg=Degrees.objects.get(doctor_id=doctor_id)
    clinic=Clinic.objects.get(doctor_id=doctor_id)
    doctor = Doctor.objects.get(user=request.user)
    specialtys = Specialization.objects.all()
    awards = Award.objects.get(doctor_id=doctor_id)
    exp = Experience.objects.get(doctor_id=doctor_id)
    doctor_ids = request.user.doctor.id
    doct=request.user
    user_id=request.user.id
    doctor=Doctor.objects.get(user_id=user_id)
    special = doctor.specialization
    service = get_object_or_404(Services, doctor=doctor_ids)
    degree = get_object_or_404(Degrees, doctor=doctor_ids)
    context={'specialtys':specialtys,'awards':awards,'exp':exp,'clinic':clinic,'doctor': doctor,'serv':serv,'deg':deg,'doctor':doctor,'degree':degree,'service':service,'special':special,'doct':doct}
     # Get the doctor instance for the logged-in user
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        doctor = Doctor.objects.get(user=request.user)
        doctor.doc_image = request.FILES.get('doc_image', doctor.doc_image)
        doctor.gender= request.POST.get('gender',doctor.gender)
        doctor.address= request.POST.get('address',doctor.address)
        doctor.biography= request.POST.get('biography',doctor.biography)
        doctor.phone= request.POST.get('phone',doctor.phone)
        doctor.city= request.POST.get('city',doctor.city)
        doctor.price= request.POST.get('price',doctor.price)
        doctor.state= request.POST.get('state',doctor.state)
        doctor.country= request.POST.get('country',doctor.country)
        doctor.date_birth= request.POST.get('date_birth',doctor.date_birth)
        doctor.status= request.POST.get('status',doctor.status)
        specialization_id= request.POST.get('specialization',doctor.specialization)
        doctor.specialization = Specialization.objects.get(id=specialization_id)
        doctor.postal_code= request.POST.get('postal_code',doctor.postal_code)
        doctor.save()
        try:
            clinic = Clinic.objects.get(doctor_id=request.user)
            clinic.clinic_name = request.POST.get('clinic_name',clinic.clinic_name)
            clinic.clinic_image = request.FILES.get('clinic_image',clinic.clinic_image)
            clinic.clinic_address = request.POST.get('clinic_address',clinic.clinic_address)
            clinic.save()
        except Clinic.DoesNotExist:
             clinic_names = request.POST.get('clinic_name','')
             clinic_images = request.FILES.get('clinic_image','')
             clinic_addresses = request.POST.get('clinic_address','')
             practic=Clinic( doctor_id=doctor_id, clinic_name=clinic_names,clinic_address=clinic_addresses, clinic_image=clinic_images )
             practic.save()
        #Degree
        try:
            degree = Degrees.objects.get(doctor_id=request.user)
            degree.degree = request.POST.get('degree',degree.degree)
            degree.institute = request.POST.get('institute',degree.institute)
            degree.year = request.POST.get('year',degree.year)
            degree.save()
        except Degrees.DoesNotExist:
            degrees = request.POST.get('degree','')
            institutes = request.POST.get('institute','')
            years = request.POST.get('year','')
            education=Degrees( doctor_id=doctor_id, degree=degrees,institute=institutes, year=years )
            education.save()
        #Experiance
        try:
           exp = Experience.objects.get(doctor_id=request.user)
           exp.hospital_name = request.POST.get('hospital_name',exp.hospital_name)
           exp.start_date = request.POST.get('start_date',exp.start_date)
           exp.end_date = request.POST.get('end_date',exp.end_date)
           designation = request.POST.get('designation',exp.designation)
           exp.save()
        except Experience.DoesNotExist:
            hospital_name = request.POST.get('hospital_name','')
            start_dates = request.POST.get('start_date','')
            end_dates = request.POST.get('end_date','')
            designation = request.POST.get('designation','')
            Exper=Experience( doctor_id=doctor_id, hospital_name=hospital_name,designation=designation,start_date=start_dates, end_date=end_dates )
            Exper.save()
        #Award inputs
        try:
           awards = Award.objects.get(doctor_id=request.user)
           awards.awards = request.POST.get('awards',awards.awards)
           awards.award_years = request.POST.get('award_year',awards.award_year)
           awards.save()
        except Award.DoesNotExist:
            awards = request.POST.get('awards','')
            award_years = request.POST.get('award_year','')
            award_instance = Award(doctor_id=doctor_id, awards=awards, award_year=award_years)
            award_instance.save()
        #Services and Specializations
        try:
           serv = Services.objects.get(doctor_id=request.user)
           serv.service = request.POST.get('service',serv.service)
           serv.save()
        except Services.DoesNotExist:
            service = request.POST.get('service','')
            service_instance = Services(doctor_id=doctor_id, service=service)
            service_instance.save()
        # Update the doctor instance with the submitted form data
        messages.success(request, 'Profile update successfully')
        
    return render(request,'doctor-profile-settings.html', context)
  else:
      return redirect('doctor_login')

def doc_appointment(request):
  if request.user.is_authenticated and request.user.is_doctor:
    doctor_id = request.user.doctor.id
    appointments_with_details = Appointment.objects.filter(doctor_id=doctor_id,status='Accepted').select_related('patient__user')
    doct=request.user
    user_id=request.user.id
    doctor=Doctor.objects.get(user_id=user_id)
    special = doctor.specialization
    service = get_object_or_404(Services, doctor=doctor_id)
    degree = get_object_or_404(Degrees, doctor=doctor_id)
    context={'doctor':doctor,'degree':degree,'service':service,'special':special,'doct':doct,'appointments_with_details':appointments_with_details,}
    return render(request,'doc_appointments.html',context)
  else:
      return redirect('doctor_login')

def update_appointment_status(request, appointment_with_detail_id, status):
  if request.user.is_authenticated and request.user.is_doctor:
    appointment = get_object_or_404(Appointment, id=appointment_with_detail_id)
    appointment.status = status
    appointment.save()
    messages.success(request,'Status update successfuly')
    return redirect('doc_panel')
  else:
      return redirect('doctor_login')

def appointment_detail_view(request, appointment_id):
   if request.user.is_authenticated and request.user.is_doctor:
    appointment = get_object_or_404(Appointment, id=appointment_id)
    doctor_id = request.user.doctor.id
    doct=request.user
    user_id=request.user.id
    doctor=Doctor.objects.get(user_id=user_id)
    special = doctor.specialization
    service = get_object_or_404(Services, doctor=doctor_id)
    degree = get_object_or_404(Degrees, doctor=doctor_id)
    context = {
        'appointment': appointment,'doctor':doctor,'degree':degree,'service':service,'special':special,'doct':doct
    }
    return render(request, 'doc_appointments.html', context)
   else:
       return redirect('doctor_login')

def my_patient(request):
  if request.user.is_authenticated and request.user.is_doctor:
    doctor_id = request.user.doctor.id
    appointments_with_details = Appointment.objects.filter(doctor_id=doctor_id).select_related('patient__user')
    doct=request.user
    user_id=request.user.id
    doctor=Doctor.objects.get(user_id=user_id)
    special = doctor.specialization
    service = get_object_or_404(Services, doctor=doctor_id)
    degree = get_object_or_404(Degrees, doctor=doctor_id)
    context={'doctor':doctor,'degree':degree,'service':service,'special':special,'doct':doct,'appointments_with_details':appointments_with_details,}
    return render(request,'my-patients.html',context)
  else:
      return redirect('doctor_login')

def doc_password_ch(request):
  if request.user.is_authenticated and request.user.is_doctor:
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        user = request.user
        # Check if the old password is correct
        if not user.check_password(old_password):
            messages.error(request, 'Incorrect old password')
            return redirect('doc_password_ch')
        # Check if the new password and confirm password match
        if new_password != confirm_password:
            messages.error(request, 'New password and confirm password do not match')
            return redirect('doc_password_ch')
        # Set the new password and save the user
        user.set_password(new_password)
        user.save()
        messages.success(request, 'Password changed successfully')
        return redirect('doc_panel')
    doctor_id = request.user.doctor.id
    doct=request.user
    user_id=request.user.id
    doctor=Doctor.objects.get(user_id=user_id)
    special = doctor.specialization
    service = get_object_or_404(Services, doctor=doctor_id)
    degree = get_object_or_404(Degrees, doctor=doctor_id)
    context={'doctor':doctor,'degree':degree,'service':service,'special':special,'doct':doct}
    return render(request,'doctor-change-password.html',context)
  else:
      return redirect('doctor_login')

def schedule_timings(request):
   if request.user.is_authenticated and request.user.is_doctor:
    doc_id=request.user.id
    doctor_ids=Doctor.objects.get(user=doc_id)
    doctor_schedule=DoctorSchedule.objects.filter(doctor_id=doctor_ids, day_of_week='Monday')
    doctor_id = request.user.doctor.id
    doct=request.user
    user_id=request.user.id
    doctor=Doctor.objects.get(user_id=user_id)
    special = doctor.specialization
    service = get_object_or_404(Services, doctor=doctor_id)
    degree = get_object_or_404(Degrees, doctor=doctor_id)
    context={'doctor':doctor,'degree':degree,'service':service,'special':special,'doct':doct,'doctor_schedule':doctor_schedule}
    return render(request,'schedule-timings.html',context)
   else:
       return redirect('doctor_login')

def add_time_slot(request):
  if request.user.is_authenticated and request.user.is_doctor:
    if request.method == 'POST':
        doc_id=request.user.id
        doctor_id=Doctor.objects.get(user=doc_id)
        day_of_week = request.POST.get('day_of_week')
        start_times = request.POST.getlist('start_time')
        end_times = request.POST.getlist('end_time')

        # Iterate over the arrays to create and save DoctorSchedule objects
        for i in range(len(start_times)):
            day_of_week = day_of_week
            start_time = start_times[i]
            end_time = end_times[i]
            
            schedule = DoctorSchedule(doctor=doctor_id, day_of_week=day_of_week, start_time=start_time, end_time=end_time)
            schedule.save()

        # Redirect to a success page or show a success message
        return redirect('schedule_timings')  # Replace 'success_page' with the URL name of your success page

    return render(request, 'schedule-timings.html')
  else:
      return redirect('doctor_login')

def doc_logout(request):
  if request.user.is_authenticated and request.user.is_doctor:
    logout(request)
    return redirect('doctor_login')
  else:
      return redirect('doctor_login')

def add_payment(request):
  if request.user.is_authenticated and request.user.is_doctor:
    if request.method=='POST':
        amount=request.POST.get('amount')
        doctor_id=request.POST.get('doctor_id')
        patient_id=request.POST.get('patient_id')
        current_date=datetime.now().date()
        doctor = Doctor.objects.get(id=doctor_id)
        patient = Patient.objects.get(id=patient_id)

        # Create the Payment instance and save it
        add_p = Payment.objects.create(amount=amount, doctor=doctor, patient=patient, payment_date=current_date)
        add_p.save()
        return redirect('doc_panel')
    else:
        return redirect('doc_appointment')
  else:
      return redirect('doctor_login')


   #patient views

def doc_forgot_password(request):
    if request.method=='POST':
        email = request.POST.get('email')
        last_name = request.POST.get('last_name')

        # Retrieve the user with the provided email and last name
        try:
            user = User.objects.get(email=email, last_name=last_name)
        except User.DoesNotExist:
            messages.error(request, 'User with the provided email and last name does not exist')
            return redirect('reset_password')

        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('con_password')

        # Check if the new password and confirm password match
        if new_password != confirm_password:
            messages.error(request, 'New password and confirm password do not match')
            return redirect('reset_password')

        # Set the new password and save the user
        user.set_password(new_password)
        user.save()

        messages.success(request, 'Password reset successfully')
        return redirect('doctor_login')
    return render(request,'doc-forgot-password.html')
def doc_forgot_password(request):
    if request.method=='POST':
        email = request.POST.get('email')
        last_name = request.POST.get('last_name')

        # Retrieve the user with the provided email and last name
        try:
            user = User.objects.get(email=email, last_name=last_name)
        except User.DoesNotExist:
            messages.error(request, 'User with the provided email and last name does not exist')
            return redirect('doc_forgot_password')

        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('con_password')

        # Check if the new password and confirm password match
        if new_password != confirm_password:
            messages.error(request, 'New password and confirm password do not match')
            return redirect('doc_forgot_password')

        # Set the new password and save the user
        user.set_password(new_password)
        user.save()

        messages.success(request, 'Password reset successfully')
        return redirect('doctor_login')
    return render(request,'doc-forgot-password.html')
def patient_forgot_password(request):
    if request.method=='POST':
        email = request.POST.get('email')
        last_name = request.POST.get('last_name')

        # Retrieve the user with the provided email and last name
        try:
            user = User.objects.get(email=email, last_name=last_name)
        except User.DoesNotExist:
            messages.error(request, 'User with the provided email and last name does not exist')
            return redirect('patient_forgot_password')

        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('con_password')

        # Check if the new password and confirm password match
        if new_password != confirm_password:
            messages.error(request, 'New password and confirm password do not match')
            return redirect('patient_forgot_password')

        # Set the new password and save the user
        user.set_password(new_password)
        user.save()

        messages.success(request, 'Password reset successfully')
        return redirect('patient_login')
    return render(request,'patient-forgot-password.html')

def view_patient(request,appointment_with_detail_id):
  if request.user.is_authenticated and request.user.is_doctor:
    doct=request.user
    user_id=request.user.id
    doctor=Doctor.objects.get(user_id=user_id)
    special = doctor.specialization
    doctor_id = request.user.doctor.id
    service = get_object_or_404(Services, doctor=doctor_id)
    degree = get_object_or_404(Degrees, doctor=doctor_id)
    appointment = get_object_or_404(Appointment, id=appointment_with_detail_id)
    appointment_with_details = Appointment.objects.select_related('doctor__user', 'patient').get(id=appointment_with_detail_id)
    context={'doctor':doctor,'degree':degree,'service':service,'special':special,'doct':doct,'appointment':appointment,'appointments':appointment_with_details}
    return render(request,'patient-profile.html',context)
  else:
      return redirect('doctor_login')


def doc_review(request):
  if request.user.is_authenticated and request.user.is_doctor:
    doct=request.user
    user_id=request.user.id
    doctor=Doctor.objects.get(user_id=user_id)
    special = doctor.specialization
    doctor_id = request.user.doctor.id
    service = get_object_or_404(Services, doctor=doctor_id)
    degree = get_object_or_404(Degrees, doctor=doctor_id)
    reviews = Review.objects.select_related('doctor__user', 'patient__user').all()
    context={'doctor':doctor,'degree':degree,'service':service,'special':special,'doct':doct,'reviews':reviews}
    return render(request,'reviews.html',context)
  else:
      return redirect('doctor_login')

def patient_logout(request):
    logout(request)
    return redirect('patient_login')
def patient_register(request):
       if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            try:
                exist=User.objects.filter(username=username)
                messages.error(request,'Username Already Exisit')
                return redirect('doctor_register')
            except User.DoesNotExist:
                  user=User.objects.create_user(is_patient=True, username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                  user.save()
                  messages.success(request,'Your Register Successfully. Login Now')
                  return redirect('add_profile')
       return render (request,'patient-register.html')

def patient_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_patient:
            login(request, user)
            try:
                patient = Patient.objects.get(user=user)
                # Redirect to profile page if patient profile exists
                return redirect('patient_panel')
            except Patient.DoesNotExist:
                # Redirect to add profile page if patient profile doesn't exist
                return redirect('add_profile')

        else:
            return redirect('patient_login')
    return render (request ,'login.html')

def add_profile(request):
    uid=request.user.id
    if request.method=='POST':
        patient_id=request.user
        # Update the patient instance with the submitted form data
        gender = request.POST.get('gender', '')
        phone = request.POST.get('phone', '')
        date_birth = request.POST.get('date_birth', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        country = request.POST.get('country', '')
        state = request.POST.get('state', '')
        postal_code = request.POST.get('postal_code', '')
        blood_group = request.POST.get('blood_group', '')  
        patient_image = request.FILES.get('patient_image', '')  # Assuming the form has a file input named 'patient_image'
        if request.user.is_authenticated and request.user.is_patient:
         profile=Patient.objects.create(user=patient_id,blood_group=blood_group,gender=gender,phone=phone,date_birth=date_birth,address=address,city=city,country=country,state=state,postal_code=postal_code,patient_image=patient_image)
         profile.save()
         return redirect('patient_panel')
        else:
            return redirect('patient_login')
    return render (request,'add-profile.html')

def patient_panel(request):
    if request.user.is_authenticated and request.user.is_patient:
        cr_user=request.user
        user_id=request.user.id
        prof=Patient.objects.get(user_id=user_id)
        today = date.today()
        age = today.year - prof.date_birth.year
        if today.month < prof.date_birth.month or (today.month == prof.date_birth.month and today.day < prof.date_birth.day):
            age -= 1
        context = {
            'age': age,
        }
        patient_id = request.user.patient.id
        appointments_with_details = Appointment.objects.filter(patient_id=patient_id).select_related('doctor__user', 'doctor__specialization')
        payments = Payment.objects.filter(patient=patient_id).select_related('patient', 'doctor__user', 'doctor__specialization')
        return render (request,'patient-dashboard.html',{'payments':payments,'appointments_with_details':appointments_with_details,'cr_user':cr_user,'prof':prof,'context':context})
    else:
        return redirect('patient_login')
    

def patient_profile(request):
   if request.user.is_authenticated and request.user.is_patient:
    user=request.user
    user_id=request.user.id
    prof=Patient.objects.get(user_id=user_id)
    today = date.today()
    age = today.year - prof.date_birth.year
    if today.month < prof.date_birth.month or (today.month == prof.date_birth.month and today.day < prof.date_birth.day):
        age -= 1
    context = {
      'prof': prof,
        'age': age,
    }

    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        patient = Patient.objects.get(user=request.user)
        patient.patient_image = request.FILES.get('patient_image', patient.patient_image)
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        patient.date_birth = request.POST.get('date_birth', patient.date_birth)
        patient.blood_group = request.POST.get('blood_group', patient.blood_group)
        patient.gender = request.POST.get('gender', patient.gender)
        patient.phone = request.POST.get('phone', patient.phone)
        patient.address = request.POST.get('address', patient.address)
        patient.city = request.POST.get('city', patient.city)
        patient.state = request.POST.get('state', patient.state)
        patient.postal_code = request.POST.get('postal_code', patient.postal_code)
        patient.country = request.POST.get('country', patient.country)
        patient.save()
        user.save()
        messages.success(request, 'Profile update successfully')
        return redirect('patient_profile')  # Replace 'profile' with the URL name of the profile page
    return render (request,'profile-settings.html',{'context':context,'user':user,'prof':prof})
   else:
    return redirect('patient_login')
 

def change_password(request):
  if request.user.is_authenticated and request.user.is_patient:
    cr_user=request.user
    user_id=request.user.id
    prof=Patient.objects.get(user_id=user_id)
    today = date.today()
    age = today.year - prof.date_birth.year
    if today.month < prof.date_birth.month or (today.month == prof.date_birth.month and today.day < prof.date_birth.day):
        age -= 1
    context = {
        'age': age,
    }
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        user = request.user

        # Check if the old password is correct
        if not user.check_password(old_password):
            messages.error(request, 'Incorrect old password')
            return redirect('change_password')

        # Check if the new password and confirm password match
        if new_password != confirm_password:
            messages.error(request, 'New password and confirm password do not match')
            return redirect('change_password')

        # Set the new password and save the user
        user.set_password(new_password)
        user.save()

        messages.success(request, 'Password changed successfully')
        return redirect('patient_panel')
    return render (request,'change-password.html',{'cr_user':cr_user,'prof':prof,'context':context})
  else:
      return redirect('patient_login')

def invoice_view(request,payment_id):
  if request.user.is_authenticated and request.user.is_patient:
    payment = get_object_or_404(Payment, id=payment_id)
    # Assuming you have ForeignKey relationships between Payment-Doctor and Payment-Patient
    # You can access related objects directly without using select_related
    doctor = payment.doctor
    patient = payment.patient

    context = {
        'payment': payment,
        'doctor': doctor,
        'patient': patient,
    }
    return render(request,'invoice-view.html',context)
  else:
      return redirect('patient_login')

def add_review(request):
  if request.user.is_authenticated and request.user.is_patient:
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        rating = request.POST.get('rating')
        title = request.POST.get('title')
        message = request.POST.get('message')
        terms_accept = request.POST.get('terms_accept')
        patient_id=request.user.patient.id

        # Check if all required fields are provided
        if doctor_id and patient_id and rating and title and message and terms_accept:
            # Create and save the review
            doctor = Doctor.objects.get(pk=doctor_id)
            patient = Patient.objects.get(pk=patient_id)
            date = datetime.now()
            review = Review.objects.create(doctor=doctor, patient=patient, date=date, message=message,title=title, rating=rating)
            review.save()

            # Redirect to a success page or perform further actions as needed
            messages.success(request,'Review send successfully')
            return redirect('search')
        else:
            # Handle the case when required fields are missing
            # Return an error message or redirect to the form page with an error flag
            messages.error(request,'Review not send')
            return redirect('search' )

    # If it's a GET request, render the form page
    
    return redirect('search')
  else:
      return redirect('patient_login')

# Chat Views
def chat(request, doctor_id):
  if request.user.is_authenticated and request.user.is_patient:  
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            doctor = User.objects.get(pk=doctor_id)
            chat = Chat.objects.create(sender=request.user, receiver=doctor, message=message)
            chat.save()

    doctor = User.objects.get(pk=doctor_id)
    chats = Chat.objects.filter(sender=request.user, receiver=doctor) | Chat.objects.filter(sender=doctor, receiver=request.user)

    # Fetch all doctors to display in the user list
    doctors = User.objects.filter(is_doctor=True)

    return render(request, 'chat.html', {'doctor': doctor, 'chats': chats, 'doctors': doctors})
  else:
     return redirect('patient_login')
def chat_doctor(request,patient_id):
   if request.user.is_authenticated and request.user.is_doctor:  
        if request.method == 'POST':
           message = request.POST.get('message')
           if message:
             patient = User.objects.get(pk=patient_id)
             chat = Chat.objects.create(sender=request.user, receiver=patient, message=message)
             chat.save()
        
        patient = User.objects.get(pk=patient_id)
        chats = Chat.objects.filter(sender=request.user, receiver=patient) | Chat.objects.filter(sender=patient, receiver=request.user)

    # Fetch all doctors to display in the user list
        patients = User.objects.filter(is_patient=True)

        return render(request, 'chat-doctor.html', {'patient': patient, 'chats': chats, 'patients': patients})
   else:
     return redirect('doctor_login')
def check_for_updates(request):
    # Check for updates in the database (you'll need to implement this logic)
    has_updates = False
    return JsonResponse({'has_updates': has_updates})