import subprocess

def reduce_cpu_usage():
  """Reduces CPU usage by disabling unnecessary services and processes."""
  # Disable unnecessary services
  subprocess.call(["sc", "config", "wuauserv", "start=disabled"])
  subprocess.call(["sc", "config", "bits", "start=disabled"])
  subprocess.call(["sc", "config", "superfetch", "start=disabled"])

  # End unnecessary processes
  subprocess.call(["taskkill", "/F", "/IM", "chrome.exe"])
  subprocess.call(["taskkill", "/F", "/IM", "firefox.exe"])
  subprocess.call(["taskkill", "/F", "/IM", "vlc.exe"])

if __name__ == "__main__":
  reduce_cpu_usage()