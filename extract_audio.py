import os,sys
from moviepy import VideoFileClip
from pathlib import Path
###################################################################
#                        从视频中提取音频                           #
#                                                                  # 
####################################################################
def extract_audio(video_path: str, output_path: str, bitrate: str = "320k"):
    """从视频中提取音频并保存为 MP3"""
    
    # 检查视频文件是否存在
    if not os.path.exists(video_path):
        print(f"❌ 错误：视频文件不存在！\n路径：{video_path}")
        return False
    
    # 检查输出文件夹是否存在，如果不存在则创建
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"📁 已创建输出文件夹：{output_dir}")
    
    print(f"🎬 正在处理视频：{video_path}")
    print(f"🎵 输出文件：{output_path}")
    
    try:
        # 加载视频
        video = VideoFileClip(video_path)
        
        if video.audio is None:
            print("❌ 错误：该视频文件中没有音频轨道！")
            video.close()
            return False
        
        print(f"📊 视频时长：{video.duration:.1f} 秒")
        print("🔄 正在提取音频，请稍等...（大文件可能需要较长时间）")
        
        # 提取并保存音频
        audio = video.audio
        audio.write_audiofile(
            output_path,
            codec='mp3',
            bitrate=bitrate,
            logger=None
        )
        
        # 释放资源
        audio.close()
        video.close()
        
        file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
        print(f"\n✅ 提取成功！")
        print(f"   文件已保存：{output_path}")
        print(f"   文件大小：{file_size_mb:.2f} MB")
        print(f"   比特率：{bitrate}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ 提取失败：{str(e)}")
        print("💡 提示：请确保已安装 FFmpeg 并添加到系统环境变量 PATH 中")
        return False


def main():
    print("=" * 60)
    print("🎵 视频音乐提取工具 v1.1")
    print("=" * 60)

    # 支持拖拽文件到终端（Windows/macOS 常用）
    if len(sys.argv) > 1:
        video_path = sys.argv[1]
        print(f"检测到拖入的文件：{video_path}")
    else:
        while True:
            video_path = input("\n请输入视频文件完整路径（或直接拖入文件）：\n> ").strip().strip('"\'')
            if os.path.exists(video_path):
                break
            print("❌ 文件不存在，请重新输入！")

    # 使用 Path 更优雅
    video_path = Path(video_path)
    default_output = video_path.with_suffix(".mp3")

    output_path = input(f"\n输出路径（默认：{default_output}）：\n> ").strip().strip('"\'')
    if not output_path:
        output_path = default_output
    else:
        output_path = Path(output_path)

    # 选择音质
    print("\n请选择音质：")
    print("1. 高音质 (320kbps) - 推荐")
    print("2. 中音质 (192kbps)")
    print("3. 低音质 (128kbps) - 文件较小")
    
    quality_choice = input("请输入选项 (1/2/3)，直接回车默认高音质：> ").strip()
    
    if quality_choice == "2":
        bitrate = "192k"
    elif quality_choice == "3":
        bitrate = "128k"
    else:
        bitrate = "320k"

    extract_audio(str(video_path), str(output_path), bitrate)

if __name__ == "__main__":
    main()




'''
@echo off
h:\DBackUp\MayaPycharm\Maya_Script\Scripts\python.exe h:\DBackUp\MayaPycharm\File_name\getMusic.py
pause

'''

