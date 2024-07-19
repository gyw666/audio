import requests
import time

# DeepLX接口列表
deepl_urls = [
    "https://translates.me/v2/translate",
    "https://deeplx.2077000.xyz:2087/translate",
    "https://deeplx.papercar.top/translate",
    "https://dlx.bitjss.com/translate",
    "https://deeplx.ychinfo.com/translate",
    "https://free-deepl.speedcow.top/translate",
    "https://deepl.coloo.org/translate",
    "https://deeplx.keyrotate.com/translate",
    "https://dx-api.nosec.link/translate",
    "https://deepx.dumpit.top/translate",
    "http://deepl.wuyongx.uk/translate",
    "https://deepl.wuyongx.uk/translate",
    "https://ghhosa.zzaning.com/translate",
    "https://deepl.zhaosaipo.com/translate",
    "https://api.deeplx.org/translate",
    "https://deeplx.he-sb.top/translate",
    "https://deepl.aimoyu.tech/translate",
    "https://deepl.tr1ck.cn/translate",
    "https://translate.dftianyi.com/translate"
]

# 测试请求参数
test_data = {
    "text": "Hello, world!",
    "source_lang": "EN",
    "target_lang": "ZH"
}

# 用来收集可用接口及其响应时间
available_endpoints = []

# 检测每个接口的可用性和延迟
for url in deepl_urls:
    try:
        start_time = time.time()
        response = requests.post(url, json=test_data, timeout=5)
        latency = time.time() - start_time
        # 确保服务真正可用
        if response.status_code == 200 and ('data' in response.json() and len(str(response.json().get("data"))) > 0):
            available_endpoints.append((url, latency))
    except requests.exceptions.RequestException:
        continue  # 忽略错误，只关注可用接口

# 根据延迟时间排序接口
available_endpoints.sort(key=lambda x: x[1])

# 打印界面美化
print("\nAvailable DeepLX Endpoints with Latencies:")
print("-" * 60)
for endpoint, delay in available_endpoints:
    print(f"🚀 ({delay:.2f}s) {endpoint}")
print("-" * 60)

# 打印所有可用的接口，按延迟排序，格式为"DeepLX👌：(count)"
if available_endpoints:
    formatted_endpoints = ", ".join([endpoint[0] for endpoint in available_endpoints])
    print(f"\nDeepLX👌：({len(available_endpoints)}) {formatted_endpoints}\n")
else:
    print("No available endpoints found.\n")