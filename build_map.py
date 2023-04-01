#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 鎶樼嚎锟�?
# x= np.linspace(0, 2, 100)

# plt.plot(x, x, label='linear')
# plt.plot(x, x**2, label='quadratic')
# plt.plot(x, x**3, label='cubic')

# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title("Simple Plot")
# plt.legend()
# plt.show()


# 绾㈣壊鐮存姌锟�?, 钃濊壊鏂瑰潡 锛岀豢鑹蹭笁瑙掑潡
# x = np.arange(0., 5., 0.2)
# plt.plot(x, x, 'r--', x, x**2, 'bs', x, x**3, 'g^')
# plt.show()


#鐩存柟锟�?
# np.random.seed(19680801)

# mu1, sigma1 = 100, 15
# mu2, sigma2 = 80, 15
# x1 = mu1 + sigma1 * np.random.randn(10000)
# x2 = mu2 + sigma2 * np.random.randn(10000)

# # the histogram of the data
# # 50锛氬皢鏁版嵁鍒嗘垚50锟�?
# # facecolor锛氶鑹诧紱alpha锛氶€忔槑锟�?
# # density锛氭槸瀵嗗害鑰屼笉鏄叿浣撴暟锟�?
# n1, bins1, patches1 = plt.hist(x1, 50, density=True, facecolor='g', alpha=1)
# n2, bins2, patches2 = plt.hist(x2, 50, density=True, facecolor='r', alpha=0.2)

# # n锛氭鐜囧€硷紱bins锛氬叿浣撴暟鍊硷紱patches锛氱洿鏂瑰浘瀵硅薄锟�?

# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.title('Histogram of IQ')

# plt.text(110, .025, r'$\mu=100,\ \sigma=15$')
# plt.text(50, .025, r'$\mu=80,\ \sigma=15$')

# # 璁剧疆x锛寉杞寸殑鍏蜂綋鑼冨洿
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)
# plt.show()


#鏌辩姸锟�?
# size = 5
# a = np.random.random(size)
# b = np.random.random(size)
# c = np.random.random(size)
# x = np.arange(size)

# # 鏈夊灏戜釜绫诲瀷锛屽彧闇€鏇存敼n鍗冲彲
# total_width, n = 0.8, 3     
# width = total_width / n

# # 閲嶆柊鎷熷畾x鐨勫潗锟�?
# x = x - (total_width - width) / 2

# # 杩欓噷浣跨敤鐨勬槸鍋忕Щ
# plt.bar(x, a,  width=width, label='a')
# plt.bar(x + width, b, width=width, label='b')
# plt.bar(x + 2 * width, c, width=width, label='c')
# plt.legend()
# plt.show()


#鍙犲姞鏌辩姸锟�?
# size = 5
# a = np.random.random(size)
# b = np.random.random(size)
# c = np.random.random(size)

# x = np.arange(size)

# # 杩欓噷浣跨敤鐨勬槸鍋忕Щ
# plt.bar(x, a, width=0.5, label='a',fc='r')
# plt.bar(x, b, bottom=a, width=0.5, label='b', fc='g')
# plt.bar(x, c, bottom=a+b, width=0.5, label='c', fc='b')

# plt.ylim(0, 2.5)
# plt.legend()
# plt.grid(True)
# plt.show()


#鏅€氶ゼ鐘跺浘
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]

# # 璁剧疆鍒嗙鐨勮窛绂伙紝0琛ㄧず涓嶅垎锟�?
# explode = (0, 0.1, 0, 0) 

# plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

# # Equal aspect ratio 淇濊瘉鐢诲嚭鐨勫浘鏄鍦嗗舰
# plt.axis('equal') 

# plt.show()


#宓屽楗肩姸
# 璁剧疆姣忕幆鐨勫锟�?
# size = 0.3
# vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

# # 閫氳繃get_cmap闅忔満鑾峰彇棰滆壊
# cmap = plt.get_cmap("tab20c")
# outer_colors = cmap(np.arange(3)*4)
# inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

# print(vals.sum(axis=1))
# # [92. 77. 39.]

# plt.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
#        wedgeprops=dict(width=size, edgecolor='w'))
# print(vals.flatten())
# # [60. 32. 37. 40. 29. 10.]

# plt.pie(vals.flatten(), radius=1-size, colors=inner_colors,
#        wedgeprops=dict(width=size, edgecolor='w'))

# # equal 浣垮緱涓烘锟�?
# plt.axis('equal') 
# plt.show()


#鏋佽酱楗肩姸锟�?
# np.random.seed(19680801)

# N = 10
# theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
# radii = 10 * np.random.rand(N)
# width = np.pi / 4 * np.random.rand(N)

# ax = plt.subplot(111, projection='polar')
# bars = ax.bar(theta, radii, width=width, bottom=0.0)
# # left琛ㄧず浠庡摢寮€濮嬶紝
# # radii琛ㄧず浠庝腑蹇冪偣鍚戣竟缂樼粯鍒剁殑闀垮害锛堝崐寰勶級
# # width琛ㄧず鏈鐨勫姬锟�?

# # 鑷畾涔夐鑹插拰涓嶉€忔槑锟�?
# for r, bar in zip(radii, bars):
#     bar.set_facecolor(plt.cm.viridis(r / 10.))
#     bar.set_alpha(0.5)

# plt.show()


#涓夌淮鏁ｇ偣锟�?
# data = np.random.randint(0, 255, size=[40, 40, 40])

# x, y, z = data[0], data[1], data[2]
# ax = plt.subplot(111, projection='3d')  # 鍒涘缓涓€涓笁缁寸殑缁樺浘宸ョ▼
# #  灏嗘暟鎹偣鍒嗘垚涓夐儴鍒嗙敾锛屽湪棰滆壊涓婃湁鍖哄垎锟�?
# ax.scatter(x[:10], y[:10], z[:10], c='y')  # 缁樺埗鏁版嵁锟�?
# ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
# ax.scatter(x[30:40], y[30:40], z[30:40], c='g')

# ax.set_zlabel('Z')  # 鍧愭爣锟�?
# ax.set_ylabel('Y')
# ax.set_xlabel('X')
# plt.show()


#涓夌淮骞抽潰锟�?
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# 鍏蜂綋鍑芥暟鏂规硶鍙敤 help(function) 鏌ョ湅锛屽锛歨elp(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()