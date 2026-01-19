# 导入图片处理库
from PIL import Image

def center_crop_img(image_path, save_path, target_width, target_height):
    """
    图片中心裁剪函数
    :param image_path: 你的图片路径(必填)
    :param save_path: 裁剪后的图片保存路径(必填)
    :param target_width: 裁剪后的目标宽度(像素)
    :param target_height: 裁剪后的目标高度(像素)
    """
    # 打开图片
    img = Image.open(image_path)
    # 获取图片原始宽高
    raw_width, raw_height = img.size
    print(f"原始图片尺寸：宽{raw_width}px × 高{raw_height}px")
    print(f"要裁剪的尺寸：宽{target_width}px × 高{target_height}px")

    # ========== 核心：中心裁剪的坐标计算（固定公式，无需修改） ==========
    # 计算裁剪的起始x坐标 = (原图宽 - 目标宽) / 2
    crop_x = (raw_width - target_width) // 2
    # 计算裁剪的起始y坐标 = (原图高 - 目标高) / 2
    crop_y = (raw_height - target_height) // 2
    # 裁剪的结束坐标
    crop_x2 = crop_x + target_width
    crop_y2 = crop_y + target_height

    # 执行裁剪（核心方法，pillow的crop传参格式：(左上x, 左上y, 右下x, 右下y)）
    crop_img = img.crop((crop_x, crop_y, crop_x2, crop_y2))
    # 保存裁剪后的图片
    crop_img.save(save_path)
    print(f"✅ 中心裁剪完成！裁剪后的图片已保存至：{save_path}")

# ==================== 这里修改成你自己的参数即可 ====================
if __name__ == "__main__":
    # 1. 你的图片路径（可以是绝对路径，比如：C:/test/1.png  或  相对路径直接写 1.png）
    IMG_PATH = "figures\chap3_aba_s2m\s2m_all.png"
    # 2. 裁剪后保存的路径（比如：crop_test.png）
    SAVE_PATH = "figures/chap3_aba_s2m/s2m_all_cropped.png"
    # 3. 你要裁剪的目标尺寸【按需修改！】
    TARGET_W = 900   # 裁剪后的宽度
    TARGET_H = 900   # 裁剪后的高度

    # 调用函数执行中心裁剪
    center_crop_img(IMG_PATH, SAVE_PATH, TARGET_W, TARGET_H)