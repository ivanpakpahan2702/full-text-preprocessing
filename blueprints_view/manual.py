from flask import Blueprint, render_template,request,jsonify
from werkzeug.utils import secure_filename
import os
import random
from _functions_.case_fold_and_punctuation_removal import *
from _functions_.normalization import *
from _functions_.stopword_filtering import *
from _functions_.stemming import *
import time

manual_blueprint = Blueprint('manual', __name__)

@manual_blueprint.route("/manual")
def manual():
    return render_template('manual.html', title="Data Mining 2023 || Manual")

@manual_blueprint.route('/manual/preprocess', methods=['GET', 'POST'])
def preprocess():
    start_time = time.time()
    # SlangFile && StopFIle Handling
    files = request.files.getlist('files[]')
    f_name = []
    for _file_ in files:
        serial_key = random.randint(10,99999)
        uploaded_folder = './static/uploads'    
        File_path = uploaded_folder + '/' + str(serial_key)+ secure_filename(_file_.filename)
        f_name.append(File_path)
        _file_.save(File_path)

    radio_sentence = int(request.values.get('radio_sentence')) 
    isCase = int(request.values.get('case_folding_stat'))
    isToken = 1
    isSlang = int(request.values.get('normalization_stat'))
    isStop =  int(request.values.get('stop_stat'))
    isStem = int(request.values.get('stem_stat'))
    main_data = (request.values.get('main_data'))
    StemLanguage = (request.values.get('stem_val'))

    print(radio_sentence)
    print(f_name)
    print(isCase)
    print(isToken)
    print(isSlang)
    print(isStop)
    print(isStem)
    print("====================================================")

    text = main_data

    if radio_sentence == 2:
        text = main_data.split('\r\n')
        if isCase == 1:
            text = [case_punc(main_data) for main_data in text]
            case_fold_text = text
        if isCase == 0:
            case_fold_text = '-'
        
        if isToken == 1:
            text = [main_data.split() for main_data in text]
            tokenize_text = text
        if isToken == 0:
            tokenize_text = '-'

        if isSlang == 1:
            text = [norm(main_data,f_name[0]) for main_data in text] 
            normalization_text = text
        if isSlang == 0:
            normalization_text = '-'

        if isStop  == 1:
            text = [stop(main_data,f_name[1]) for main_data in text]
            filtering_text = text
        if isStop == 0:
            filtering_text = '-'
        
        if isStem == 1:
            text = [stem(main_data,StemLanguage) for main_data in text]
            stemming_text = text
        if isStem == 0:
            stemming_text = '-'
        
        result = text
    
    elif radio_sentence == 1:
        if isCase == 1:
            text = case_punc(main_data)
            case_fold_text = text
        if isCase == 0:
            case_fold_text = '-'

        if isToken == 1:
            text = text.split()
            tokenize_text = text
        if isToken == 0:
            tokenize_text = '-'
        
        if isSlang == 1:
            text = norm(text,f_name[0])
            normalization_text = text
        if isSlang == 0:
            normalization_text = '-'
        
        if isStop  == 1:
            text = stop(text,f_name[1])
            filtering_text = text
        if isStop == 0:
            filtering_text = '-'
        
        if isStem == 1:
            text = stem(text,StemLanguage)
            stemming_text = text
        if isStem == 0:
            stemming_text = '-'
        
        result = text

    for file_name in f_name:
        os.remove(file_name)
        print(file_name+" Deleted!")
    
    process_time = (time.time() - start_time)
    process_time = str(process_time)


    return jsonify([str(case_fold_text),str(tokenize_text),str(normalization_text),str(filtering_text),str(stemming_text),str(result),process_time[:6]])