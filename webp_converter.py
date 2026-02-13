import os
from PIL import Image

def convert_webp_to_format(input_dir, output_format='png'):
    # 确保输出格式是有效的
    if output_format not in ['png', 'jpg']:
        print('错误: 输出格式必须是 png 或 jpg')
        return
    
    # 确保输入目录存在
    if not os.path.exists(input_dir):
        print(f'错误: 目录 {input_dir} 不存在')
        return
    
    # 创建输出目录
    output_dir = os.path.join(os.path.dirname(input_dir), f'output_{output_format}')
    os.makedirs(output_dir, exist_ok=True)
    
    # 遍历目录中的所有文件
    for filename in os.listdir(input_dir):
        # 检查文件是否是 webp 格式
        if filename.lower().endswith('.webp'):
            # 构建完整的文件路径
            input_path = os.path.join(input_dir, filename)
            
            # 构建输出文件名
            output_filename = os.path.splitext(filename)[0] + f'.{output_format}'
            output_path = os.path.join(output_dir, output_filename)
            
            try:
                # 打开并转换图片
                with Image.open(input_path) as img:
                    # 如果是 jpg 格式，确保图片模式正确
                    if output_format == 'jpg':
                        # 确定保存格式
                        save_format = 'JPEG'
                        # 如果是 RGBA 模式，需要添加白色背景
                        if img.mode == 'RGBA':
                            # 创建白色背景
                            background = Image.new('RGB', img.size, (255, 255, 255))
                            # 粘贴图片到背景上
                            background.paste(img, mask=img.split()[3])
                            background.save(output_path, save_format, quality=95)
                        else:
                            img.save(output_path, save_format, quality=95)
                    else:  # png 格式
                        img.save(output_path, output_format.upper())
                print(f'成功转换: {filename} -> {output_filename}')
            except Exception as e:
                print(f'转换失败 {filename}: {str(e)}')

if __name__ == '__main__':
    # 定义 webp 目录路径
    webp_dir = os.path.join(os.path.dirname(__file__), 'webp')
    
    # 询问用户选择输出格式
    while True:
        format_choice = input('请选择输出格式 (png/jpg): ').lower()
        if format_choice in ['png', 'jpg']:
            break
        print('请输入有效的格式选项')
    
    # 执行转换
    print(f'开始将 webp 文件转换为 {format_choice} 格式...')
    convert_webp_to_format(webp_dir, format_choice)
    print('转换完成!')