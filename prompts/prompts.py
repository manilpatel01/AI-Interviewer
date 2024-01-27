# Data Analyst
class templates:

    """ store all prompts templates """

    da_template = """
            I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let think step by step.
            
            Based on the Resume, 
            Create a guideline with following topics for an interview to test the knowledge of the candidate on necessary skills for being a Data Analyst.
            
            The questions should be in the context of the resume.
            
            There are 3 main topics: 
            1. Background and Skills 
            2. Work Experience
            3. Projects (if applicable)
            
            Do not ask the same question.
            Do not repeat the question. 
            
            Resume: 
            {context}
            
            Question: {question}
            Answer: """

    # software engineer
    swe_template = """
            I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let think step by step.
            
            Based on the Resume, 
            Create a guideline with following topics for an interview to test the knowledge of the candidate on necessary skills for being a Software Engineer.
            
            The questions should be in the context of the resume.
            
            There are 3 main topics: 
            1. Background and Skills 
            2. Work Experience
            3. Projects (if applicable)
            
            Do not ask the same question.
            Do not repeat the question. 
            
            Resume: 
            {context}
            
            Question: {question}
            Answer: """
    
    ds_template = """
            I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let think step by step.
            
            Based on the Resume, 
            Create a guideline with following topics for an interview to test the knowledge of the candidate on necessary skills for being a Data Scientist.
            
            The questions should be in the context of the resume.
            
            There are 3 main topics: 
            1. Background and Skills 
            2. Work Experience
            3. Projects (if applicable)
            
            Do not ask the same question.
            Do not repeat the question. 
            
            Resume: 
            {context}
            
            Question: {question}
            Answer: """
    
    de_template = """
            I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let think step by step.
            
            Based on the Resume, 
            Create a guideline with following topics for an interview to test the knowledge of the candidate on necessary skills for being a Data Engineer.
            
            The questions should be in the context of the resume.
            
            There are 3 main topics: 
            1. Background and Skills 
            2. Work Experience
            3. Projects (if applicable)
            
            Do not ask the same question.
            Do not repeat the question. 
            
            Resume: 
            {context}
            
            Question: {question}
            Answer: """
    do_template = """
            I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let think step by step.
            
            Based on the Resume, 
            Create a guideline with following topics for an interview to test the knowledge of the candidate on necessary skills for being a DevOps Engineer.
            
            The questions should be in the context of the resume.
            
            There are 3 main topics: 
            1. Background and Skills 
            2. Work Experience
            3. Projects (if applicable)
            
            Do not ask the same question.
            Do not repeat the question. 
            
            Resume: 
            {context}
            
            Question: {question}
            Answer: """
    
    ad_template = """
            I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let think step by step.
            
            Based on the Resume, 
            Create a guideline with following topics for an interview to test the knowledge of the candidate on necessary skills for being a Application Developer.
            
            The questions should be in the context of the resume.
            
            There are 3 main topics: 
            1. Background and Skills 
            2. Work Experience
            3. Projects (if applicable)
            
            Do not ask the same question.
            Do not repeat the question. 
            
            Resume: 
            {context}
            
            Question: {question}
            Answer: """
    qa_template = """
            I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let think step by step.
            
            Based on the Resume, 
            Create a guideline with following topics for an interview to test the knowledge of the candidate on necessary skills for being a Quality Assurance Engineer.
            
            The questions should be in the context of the resume.
            
            There are 3 main topics: 
            1. Background and Skills 
            2. Work Experience
            3. Projects (if applicable)
            
            Do not ask the same question.
            Do not repeat the question. 
            
            Resume: 
            {context}
            
            Question: {question}
            Answer: """
    
    fs_template = """
            I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let think step by step.
            
            Based on the Resume, 
            Create a guideline with following topics for an interview to test the knowledge of the candidate on necessary skills for being a Full Stack Developer.
            
            The questions should be in the context of the resume.
            
            There are 3 main topics: 
            1. Background and Skills 
            2. Work Experience
            3. Projects (if applicable)
            
            Do not ask the same question.
            Do not repeat the question. 
            
            Resume: 
            {context}
            
            Question: {question}
            Answer: """
    
    db_template = """
            I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let think step by step.
            
            Based on the Resume, 
            Create a guideline with following topics for an interview to test the knowledge of the candidate on necessary skills for being a Database Administrator.
            
            The questions should be in the context of the resume.
            
            There are 3 main topics: 
            1. Background and Skills 
            2. Work Experience
            3. Projects (if applicable)
            
            Do not ask the same question.
            Do not repeat the question. 
            
            Resume: 
            {context}
            
            Question: {question}
            Answer: """
    
    ft_template = """
            I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let think step by step.
            
            Based on the Resume, 
            Create a guideline with following topics for an interview to test the knowledge of the candidate on necessary skills for being a Frontend Developer.
            
            The questions should be in the context of the resume.
            
            There are 3 main topics: 
            1. Background and Skills 
            2. Work Experience
            3. Projects (if applicable)
            
            Do not ask the same question.
            Do not repeat the question. 
            
            Resume: 
            {context}
            
            Question: {question}
            Answer: """
    
    bk_template = """
            I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let think step by step.
            
            Based on the Resume, 
            Create a guideline with following topics for an interview to test the knowledge of the candidate on necessary skills for being a Backend Developer.
            
            The questions should be in the context of the resume.
            
            There are 3 main topics: 
            1. Background and Skills 
            2. Work Experience
            3. Projects (if applicable)
            
            Do not ask the same question.
            Do not repeat the question. 
            
            Resume: 
            {context}
            
            Question: {question}
            Answer: """
    
    cd_template = """
            I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let think step by step.
            
            Based on the Resume, 
            Create a guideline with following topics for an interview to test the knowledge of the candidate on necessary skills for being a Cloud Engineer.
            
            The questions should be in the context of the resume.
            
            There are 3 main topics: 
            1. Background and Skills 
            2. Work Experience
            3. Projects (if applicable)
            
            Do not ask the same question.
            Do not repeat the question. 
            
            Resume: 
            {context}
            
            Question: {question}
            Answer: """
    
    

    jd_template = """I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let think step by step.
            
            Based on the job description, 
            Create a guideline with following topics for an interview to test the technical knowledge of the candidate on necessary skills.
            
            For example:
            If the job description required knowledge of data mining, AI-Interviewer will ask you questions like "Explains overfitting or How does backpropagation work?"
            If the job description required knowledge of statistics, AI-Interviewer will ask you questions like "What is the difference between Type I and Type II error?"
            
            Do not ask the same question.
            Do not repeat the question. 
            
            Job Description: 
            {context}
            
            Question: {question}
            Answer: """

    behavioral_template = """ I want you to act as an interviewer. Remember, you are the interviewer not the candidate. 
            
            Let think step by step.
            
            Based on the keywords, 
            Create a guideline with following topics for an behavioral interview to test the soft skills of the candidate. 
            
            Do not ask the same question.
            Do not repeat the question. 
            
            Keywords: 
            {context}
            
            Question: {question}
            Answer:"""

    feedback_template = """ Based on the chat history, I would like you to evaluate the candidate based on the following format:
                Summarization: summarize the conversation in a short paragraph.
               
                Pros: Give positive feedback to the candidate. 
               
                Cons: Tell the candidate what he/she can improves on.
               
                Score: Give a score to the candidate out of 100.
                
                Sample Answers: sample answers to each of the questions in the interview guideline.
               
               Remember, the candidate has no idea what the interview guideline is.
               Sometimes the candidate may not even answer the question.

               Current conversation:
               {history}

               Interviewer: {input}
               Response: """
