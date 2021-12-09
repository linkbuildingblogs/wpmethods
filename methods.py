"""
THIS FILE HANDLES POSTING PAGES , POSTING BLOGS , CREATING CATEGORY , UPDATE SITE TITLE AND DESCRIPTION
AUTHOR : SOURAV PADHI
ORG : LINK BUILDING BLOGS
CONTRIBUTOR : FALAK BHARDWAJ
"""
import requests
import json
import base64
import pymysql


def postpage(weburl , wpuser , wppass , metatitle , metadesc , host , dbuser , dbpass , dbname , dbprefix , postcontent , postslug , poststatus , posttitle):
    #STRUCTURES THE URL FOR THE PURPOSE , /PAGES INDICATES THE METHOD OF POSTING PAGES AND THE BASE "/wp-json/wp/v2/" IS UNITARY 
    url = weburl+'/wp-json/wp/v2/pages'
    #CASTS A DATABSE CONNECTION WITH THE PROGRAM , USES *pymysql*
    connection = pymysql.connect(host=host,user=dbuser,passwd=dbpass,database=dbname)
    #INITITATES THE CONNECTION
    cursor = connection.cursor()
    #'content' REPRESENTS THE PAGE / POST CONTENT
    #'description' REPRESENTS THE PAGE DESCRIPTION NOT META DESCRIPTION
    #'slug' REPRESENTS THE POST TYPE SLUG
    #'status' REPRESENTS THE POST STATUS
    #'title' REPRESENTS THE POST TITLE
    data = {'content': postcontent, 'meta': {'description': 'this is a test meta field'}, 'slug': postslug, 'status': poststatus,'title': posttitle}
    # A REQUEST WITH BASIC AUTH 
    resp = requests.post(url, json=data, auth=(wpuser,wppass), headers={'Content-Type':'application/json'})
    pageid = str(resp.json()['id'])
    cursor.execute("INSERT INTO "+dbprefix+"_postmeta"+"(meta_id, post_id, meta_key, meta_value) VALUES (\'\', \'{0}\' , \'rank_math_title\' , \'{1}\') , ( \'\', \'{0}\' , \'rank_math_description\' ,\'{2}\')".format(pageid , metatitle, metadesc))
    ans = cursor.fetchall() 
    print(ans)
    connection.commit()
    
def postblog(weburl , wpuser , wppass , metatitle , metadesc , host , dbuser , dbpass , dbname , dbprefix , postcontent , postslug , poststatus , posttitle):
    #STRUCTURES THE URL FOR THE PURPOSE , /PAGES INDICATES THE METHOD OF POSTING PAGES AND THE BASE "/wp-json/wp/v2/" IS UNITARY 
    url = weburl+'/wp-json/wp/v2/posts'
    #CASTS A DATABSE CONNECTION WITH THE PROGRAM , USES *pymysql*
    connection = pymysql.connect(host=host,user=dbuser,passwd=dbpass,database=dbname)
    #INITITATES THE CONNECTION
    cursor = connection.cursor()
    #'content' REPRESENTS THE PAGE / POST CONTENT
    #'description' REPRESENTS THE PAGE DESCRIPTION NOT META DESCRIPTION
    #'slug' REPRESENTS THE POST TYPE SLUG
    #'status' REPRESENTS THE POST STATUS
    #'title' REPRESENTS THE POST TITLE
    data = {'content': postcontent, 'meta': {'description': 'this is a test meta field'}, 'slug': postslug, 'status': poststatus,'title': posttitle}
    # A REQUEST WITH BASIC AUTH 
    resp = requests.post(url, json=data, auth=(wpuser,wppass), headers={'Content-Type':'application/json'})
    pageid = str(resp.json()['id'])
    # A BASIC EXECUTION OF A SQL QUERY DIRECTLY UPDATING THE SQL VALUES OF THE PLUGIN DEPENDENT TABLES
    cursor.execute("INSERT INTO "+dbprefix+"_postmeta"+"(meta_id, post_id, meta_key, meta_value) VALUES (\'\', \'{0}\' , \'rank_math_title\' , \'{1}\') , ( \'\', \'{0}\' , \'rank_math_description\' ,\'{2}\')".format(pageid , metatitle, metadesc))
    ans = cursor.fetchall() 
    print(ans)
    connection.commit()
    
def create_cat(categoryname , host , dbuser , dbpass , dbname , dbprefix ):
    #CASTS A DATABSE CONNECTION WITH THE PROGRAM , USES *pymysql*
    connection = pymysql.connect(host=host,user=dbuser,passwd=dbpass,database=dbname)
    #INITITATES THE CONNECTION
    cursor = connection.cursor()
    # A BASIC EXECUTION OF A SQL QUERY DIRECTLY UPDATING THE SQL VALUES OF THE PLUGIN DEPENDENT TABLES
    cursor.execute("INSERT INTO "+dbprefix+"_postmeta"+"(term_id , name , slug , term_group) VALUES ('' , '{0}' , '{1}' , '{2}')".format(categoryname , categoryname, "0"))
    #TO SAVE CHANGES WE USE .commit METHOD
    connection.commit()
    cursor.execute("SELECT term_id FROM "+dbprefix+"_postmeta"+" WHERE name = '{0}'".format(categoryname))
    out = cursor.fetchall() 
    term_id = list(out[0])
    # A BASIC EXECUTION OF A SQL QUERY DIRECTLY UPDATING THE SQL VALUES OF THE PLUGIN DEPENDENT TABLES
    cursor.execute("INSERT INTO "+dbprefix+"_postmeta"+" (term_taxonomy_id, term_id, taxonomy, description, parent, count) VALUES (NULL, '{0}', 'category', '', '0', '0')".format(term_id[0]))
    connection.commit()
    
def update_site(BlogName , BlogDesc , host , dbuser , dbpass , dbname , dbprefix ):
    #CASTS A DATABSE CONNECTION WITH THE PROGRAM , USES *pymysql*
    connection = pymysql.connect(host=host,user=dbuser,passwd=dbpass,database=dbname)
    #INITITATES THE CONNECTION
    cursor = connection.cursor()
    cursor.execute("UPDATE "+dbprefix+"`_options` SET `option_value` = '{0}' WHERE "+dbprefix+"`_options`.`option_id` = 3;".format(BlogName))
    #TO SAVE CHANGES WE USE .commit METHOD
    connection.commit()
    cursor.execute("UPDATE "+dbprefix+"`_options` SET `option_value` = '{0}' WHERE "+dbprefix+"`_options`.`option_id` = 4;".format(BlogDesc))
    #TO SAVE CHANGES WE USE .commit METHOD
    connection.commit()
    
    
def postblog_2(weburl , wpuser , wppass , postcontent , postslug , poststatus , posttitle):
    #STRUCTURES THE URL FOR THE PURPOSE , /PAGES INDICATES THE METHOD OF POSTING PAGES AND THE BASE "/wp-json/wp/v2/" IS UNITARY 
    url = weburl+'/wp-json/wp/v2/posts'
    #CASTS A DATABSE CONNECTION WITH THE PROGRAM , USES *pymysql*
    #'content' REPRESENTS THE PAGE / POST CONTENT
    #'description' REPRESENTS THE PAGE DESCRIPTION NOT META DESCRIPTION
    #'slug' REPRESENTS THE POST TYPE SLUG
    #'status' REPRESENTS THE POST STATUS
    #'title' REPRESENTS THE POST TITLE
    data = {'content': postcontent, 'meta': {'description': 'this is a test meta field'}, 'slug': postslug, 'status': poststatus,'title': posttitle}
    # A REQUEST WITH BASIC AUTH 
    resp = requests.post(url, json=data, auth=(wpuser,wppass), headers={'Content-Type':'application/json'})
    
    
    
