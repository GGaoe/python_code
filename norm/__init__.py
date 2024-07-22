from .url_manager import URLmanager

__all__ = ['URLmanager']

def main():
    # 假设 URLmanager 有一个名为 run 的方法
    manager = URLmanager()
    manager.run()

if __name__ == "__main__":
    main()