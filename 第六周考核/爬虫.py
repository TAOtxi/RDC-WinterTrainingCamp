import pymysql
import urllib.request
import re

url = [
      'https://www.douyin.com/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7199202031431617832&cursor=0&count=20&item_type=0&insert_ids=&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=110.0.0.0&browser_online=true&engine_name=Blink&engine_version=110.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7172740562112562723&msToken=oz8fKE1IecMWzxz3icRkopf5IsmQ40AeBYX_uHnG5fYQv0Dcdr88fGdXDnmEgFwxMIgD1YJK5o6UCgW-Ho9ByhfLS7txxl5OWUTykSjEa4MAYHCeeXrEVQ==&X-Bogus=DFSzswVLM8zANcXnShzZGe9WX7jr',
       'https://www.douyin.com/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7199202031431617832&cursor=20&count=20&item_type=0&insert_ids=&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=110.0.0.0&browser_online=true&engine_name=Blink&engine_version=110.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7172740562112562723&msToken=oTrt7mllhyi6JB9RbuFVu3zRg4PfnomEw052zyuIvriWS-uIEMRdHoE-k2GAHBSS5Ox8rgcPdjU_Jjj8x8RIL02Dww13lMoFvKg5mlnHhgdeZF1X5BhOMQ==&X-Bogus=DFSzswVL5vTANcXnShzkLe9WX7rh',
      'https://www.douyin.com/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7199202031431617832&cursor=40&count=20&item_type=0&insert_ids=&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=110.0.0.0&browser_online=true&engine_name=Blink&engine_version=110.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7172740562112562723&msToken=uioUccVPgo2id-pzRhyVb56rdMdjjIrRB0Wg8xGMJ_K42_qK4m8CwcErmfqhOn8d5wfseirr4Q-38ZedSzEt6a6RFLmsX7k-2sYkFsWSa-swaDYrXUp3NA==&X-Bogus=DFSzswVL0ThANcXnShzp/M9WX7nV',
      'https://www.douyin.com/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7199202031431617832&cursor=60&count=20&item_type=0&insert_ids=&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=110.0.0.0&browser_online=true&engine_name=Blink&engine_version=110.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7172740562112562723&msToken=uioUccVPgo2id-pzRhyVb56rdMdjjIrRB0Wg8xGMJ_K42_qK4m8CwcErmfqhOn8d5wfseirr4Q-38ZedSzEt6a6RFLmsX7k-2sYkFsWSa-swaDYrXUp3NA==&X-Bogus=DFSzswVLZ8GANcXnShzp0F9WX7rp', 'https://www.douyin.com/aweme/v1/web/comment/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id=7199202031431617832&cursor=80&count=20&item_type=0&insert_ids=&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=110.0.0.0&browser_online=true&engine_name=Blink&engine_version=110.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7172740562112562723&msToken=uioUccVPgo2id-pzRhyVb56rdMdjjIrRB0Wg8xGMJ_K42_qK4m8CwcErmfqhOn8d5wfseirr4Q-38ZedSzEt6a6RFLmsX7k-2sYkFsWSa-swaDYrXUp3NA==&X-Bogus=DFSzswVLSJtANcXnShzp0M9WX7re'
]
headers = {
    #'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'bd-ticket-guard-client-cert': 'LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUNFekNDQWJxZ0F3SUJBZ0lVZm4yQmxZYTVoRk4xSXpBNkYwUk0yL2VaUFcwd0NnWUlLb1pJemowRUF3SXcKTVRFTE1Ba0dBMVVFQmhNQ1EwNHhJakFnQmdOVkJBTU1HWFJwWTJ0bGRGOW5kV0Z5WkY5allWOWxZMlJ6WVY4eQpOVFl3SGhjTk1qTXdNakUyTVRJeE1UQTRXaGNOTXpNd01qRTJNakF4TVRBNFdqQW5NUXN3Q1FZRFZRUUdFd0pEClRqRVlNQllHQTFVRUF3d1BZbVJmZEdsamEyVjBYMmQxWVhKa01Ga3dFd1lIS29aSXpqMENBUVlJS29aSXpqMEQKQVFjRFFnQUVQd3dRbUZSN05jOEtXaWwwZDFVRnZuSDlVYWh3MW0vdzRRd1Z5blBBdmg4LzBwZm9keDVuYVl5Wgo3NlMvRHRPVzVxOW4xcGNGVGZPN1lKTXFwSVRxNHFPQnVUQ0J0akFPQmdOVkhROEJBZjhFQkFNQ0JhQXdNUVlEClZSMGxCQ293S0FZSUt3WUJCUVVIQXdFR0NDc0dBUVVGQndNQ0JnZ3JCZ0VGQlFjREF3WUlLd1lCQlFVSEF3UXcKS1FZRFZSME9CQ0lFSUQ3WDFVeExsU1lQMU1RN0RWc2dYRlZDb2Vyd25STlhzZXM0RG03U2tWaFJNQ3NHQTFVZApJd1FrTUNLQUlES2xaK3FPWkVnU2pjeE9UVUI3Y3hTYlIyMVRlcVRSZ05kNWxKZDdJa2VETUJrR0ExVWRFUVFTCk1CQ0NEbmQzZHk1a2IzVjVhVzR1WTI5dE1Bb0dDQ3FHU000OUJBTUNBMGNBTUVRQ0lFbU5aNlc2YTRLcmhGRVUKc3lhUXRpOTUzSDJVMElhcytZa3ppMk5XVkpwbEFpQmhZUG5HRkZ2U2k0TERvd0wvSFJzYi9ieks0d1kxZDFWVwpGOGNJWk45c3hnPT0KLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=',
    'bd-ticket-guard-client-data': 'eyJ0c19zaWduIjoiY29tcHJlc3NOWWZ1d2NSTFdMYTB1dUZWTks0SmRkRTFOeEdPL2dmSU9ERWNUcG5sWDdBPSIsInJlcV9jb250ZW50IjoiYjllZmY5YzRlMDkzMTdjYjhkNzRhMzA5YTcyNjI4NjIiLCJyZXFfc2lnbiI6Ik1FWUNJUURHaS9WTzRFTEZ0eE5SZm81NGNNVkFHc1RpNGJoeFNlU1VER1RQWFVpcDRRSWhBSWM4Mm1XbXNpOHFiWUN5WWNVMHNWS0dqaW1zcENTVWhTOEUzS2s4QnZVSyIsInRpbWVzdGFtcCI6MTY3NjYzODQ5OX0=',
    'bd-ticket-guard-version': '2',
    'cookie': 'ttwid=1%7CIzbevUXtpbr6aqIUrBn_xNGmdUzhGv_Qzy9a5Wf_4So%7C1670033830%7C2594cc918ce917dc886bb030cd3d3cd93828b4910d77fb4157d30b576ec207e9; passport_csrf_token=4e486eaa45c2385cc4fb7733c3da8d95; passport_csrf_token_default=4e486eaa45c2385cc4fb7733c3da8d95; s_v_web_id=verify_le71p9ac_IBskEqCF_4OmK_4f7w_B8ut_a752LmuVd87j; xgplayer_user_id=651594855596; n_mh=P1gXSEZ8ejdVWLryB-ca1wUf3nPHZ2d8OwNVC88Ejb4; sso_uid_tt=4f464c11e65d1a1364948f0d8bbc2276; sso_uid_tt_ss=4f464c11e65d1a1364948f0d8bbc2276; toutiao_sso_user=8b28efb871a110574063d4028a36e125; toutiao_sso_user_ss=8b28efb871a110574063d4028a36e125; sid_ucp_sso_v1=1.0.0-KDA3YjExYTRjYjk4ZmNkOWNhZDdmMDE5MWI2MDUyN2E3MGE0M2U4YWEKHQip1q_l4wIQ27q4nwYY7zEgDDD_-q7VBTgGQPQHGgJobCIgOGIyOGVmYjg3MWExMTA1NzQwNjNkNDAyOGEzNmUxMjU; ssid_ucp_sso_v1=1.0.0-KDA3YjExYTRjYjk4ZmNkOWNhZDdmMDE5MWI2MDUyN2E3MGE0M2U4YWEKHQip1q_l4wIQ27q4nwYY7zEgDDD_-q7VBTgGQPQHGgJobCIgOGIyOGVmYjg3MWExMTA1NzQwNjNkNDAyOGEzNmUxMjU; passport_assist_user=CjyKagG21EqCcKob1UjBxAZMp6ZDCqgebe7CXHPbNb46mQohqqk-dmljygGrS6IwbgiamORBOwZpx-ZbyN0aSAo8-mWyIjvHcpZtvv_ElynyBH6kzZ6-tz5oTOh3AuzMsnvNJ0vfQjYRbA-aSkXBGVt6ScVW9yanXgVQPuJwEM66qQ0Yia_WVCIBA4RQUXU%3D; odin_tt=34b7faa4ac07762cb8ed5d173d98e3ccc612b2a2916d8b6f69cecd1f78dcfdf69c7aad165ca3be585393fd1d803cfdc5; passport_auth_status=1b719a05046098d2f05b0d0fc92d703b%2C; passport_auth_status_ss=1b719a05046098d2f05b0d0fc92d703b%2C; uid_tt=5b402aab453ae8b565c69b9098c3ddb5; uid_tt_ss=5b402aab453ae8b565c69b9098c3ddb5; sid_tt=b9eff9c4e09317cb8d74a309a7262862; sessionid=b9eff9c4e09317cb8d74a309a7262862; sessionid_ss=b9eff9c4e09317cb8d74a309a7262862; _tea_utm_cache_2018=undefined; LOGIN_STATUS=1; store-region=cn-gd; store-region-src=uid; sid_guard=b9eff9c4e09317cb8d74a309a7262862%7C1676549478%7C5183989%7CMon%2C+17-Apr-2023+12%3A11%3A07+GMT; sid_ucp_v1=1.0.0-KGU1NTk1MWNjODJjNjE5ZTg1MTYyZTMwMWRhZjI3YjhjMTk0OWM3NDEKGQip1q_l4wIQ5rq4nwYY7zEgDDgGQPQHSAQaAmhsIiBiOWVmZjljNGUwOTMxN2NiOGQ3NGEzMDlhNzI2Mjg2Mg; ssid_ucp_v1=1.0.0-KGU1NTk1MWNjODJjNjE5ZTg1MTYyZTMwMWRhZjI3YjhjMTk0OWM3NDEKGQip1q_l4wIQ5rq4nwYY7zEgDDgGQPQHSAQaAmhsIiBiOWVmZjljNGUwOTMxN2NiOGQ3NGEzMDlhNzI2Mjg2Mg; d_ticket=a1157be679599a6a1e069d4bb2c8eb8ddbf3e; download_guide=%223%2F20230216%22; douyin.com; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWNsaWVudC1jZXJ0IjoiLS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tXG5NSUlDRXpDQ0FicWdBd0lCQWdJVWZuMkJsWWE1aEZOMUl6QTZGMFJNMi9lWlBXMHdDZ1lJS29aSXpqMEVBd0l3XG5NVEVMTUFrR0ExVUVCaE1DUTA0eElqQWdCZ05WQkFNTUdYUnBZMnRsZEY5bmRXRnlaRjlqWVY5bFkyUnpZVjh5XG5OVFl3SGhjTk1qTXdNakUyTVRJeE1UQTRXaGNOTXpNd01qRTJNakF4TVRBNFdqQW5NUXN3Q1FZRFZRUUdFd0pEXG5UakVZTUJZR0ExVUVBd3dQWW1SZmRHbGphMlYwWDJkMVlYSmtNRmt3RXdZSEtvWkl6ajBDQVFZSUtvWkl6ajBEXG5BUWNEUWdBRVB3d1FtRlI3TmM4S1dpbDBkMVVGdm5IOVVhaHcxbS93NFF3VnluUEF2aDgvMHBmb2R4NW5hWXlaXG43NlMvRHRPVzVxOW4xcGNGVGZPN1lKTXFwSVRxNHFPQnVUQ0J0akFPQmdOVkhROEJBZjhFQkFNQ0JhQXdNUVlEXG5WUjBsQkNvd0tBWUlLd1lCQlFVSEF3RUdDQ3NHQVFVRkJ3TUNCZ2dyQmdFRkJRY0RBd1lJS3dZQkJRVUhBd1F3XG5LUVlEVlIwT0JDSUVJRDdYMVV4TGxTWVAxTVE3RFZzZ1hGVkNvZXJ3blJOWHNlczREbTdTa1ZoUk1Dc0dBMVVkXG5Jd1FrTUNLQUlES2xaK3FPWkVnU2pjeE9UVUI3Y3hTYlIyMVRlcVRSZ05kNWxKZDdJa2VETUJrR0ExVWRFUVFTXG5NQkNDRG5kM2R5NWtiM1Y1YVc0dVkyOXRNQW9HQ0NxR1NNNDlCQU1DQTBjQU1FUUNJRW1OWjZXNmE0S3JoRkVVXG5zeWFRdGk5NTNIMlUwSWFzK1lremkyTldWSnBsQWlCaFlQbkdGRnZTaTRMRG93TC9IUnNiL2J6SzR3WTFkMVZXXG5GOGNJWk45c3hnPT1cbi0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS1cbiJ9; csrf_session_id=53f71a43a5277ae312651ee9ba1fddbe; strategyABtestKey=%221676619713.246%22; __ac_signature=_02B4Z6wo00f01HqrEcwAAIDA-qnrjfSIlLR6ixVAAH1NIJ0ejL7Z8cQlMqxaHvHylrdEZtDxGHtKwa-rO-43OdB2eh3F-boFl04Hr2gW7a1QjefLoXzNvnMa-eDwtcMfE7vW-nk4POEbRUZa71; my_rd=1; passport_fe_beating_status=true; home_can_add_dy_2_desktop=%221%22; tt_scid=yxPhxpiGyYnMZ2aX3i60oEypPmMBp14fldGxAUmrTiJZQPU4f72Z9qmHfPoqjYHR739c; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAMrUjboip531j0FuST67bTzJ8qV6VN8wQ5_rKwe1ZIcA%2F1676649600000%2F0%2F0%2F1676638711364%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAMrUjboip531j0FuST67bTzJ8qV6VN8wQ5_rKwe1ZIcA%2F1676649600000%2F0%2F0%2F1676639311365%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1677242913957%2C%22type%22%3A0%7D; msToken=BuE8JHmMMq1zgpRT_cLlOCrcRNxM_dEVyeu105gYOhcAU0V3NrliRAc6oOHMlWMRb1QOD7Sxgv0Izdr6anYiv6MUgJ2_mJF86-E6yJFNr9EO3aQONRQPFw==; msToken=IhrwBM9Ey700XurK0Ty6vVk8w1JC91sYYGQBUdcoi_C-Jabrv3we2jlwbjLgaWE1VZfHGZ4p3NBZGELbwh2esd9rD0Cxq0TFCKRu2rjzz_QeRcj82epVrw==',
    'referer': 'https://www.douyin.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}
pachong = []
for i in range(5):
      request = urllib.request.Request(url=url[i], headers=headers)
      response = urllib.request.urlopen(request)
      content = response.read().decode('utf-8')
      content = re.findall(r'"create_time":(\d+).*?'
                           '"ip_label":"(.*?)".*?'
                           '"text":"(.*?)".*?'
                           '"nickname":"(.*?)".*?'
                           '"signature":"(.*?)".*?'
                           '"unique_id":"(.*?)",', content, re.S)
      pachong = pachong + content
print('-' * 60)

db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='TEST')

cursor = db.cursor()
sql ='''create table if not exists comment(
        time bigint comment '评论时间',
        ip_location char(10) comment 'ip地址',
        comment varchar(200) comment '评论',
        nickname char(20) comment '昵称',
        signature varchar(100) comment '个人简介',
        unique_id char(20) comment 'uid' 
        )'''

cursor.execute(sql)
for i in pachong:
    sql = 'insert into comment values ' + str(i)
    cursor.execute(sql)
    # print(i)
db.commit()
db.close()