from same_game import controller, metrics
import graphics


try:
    controller.agentVSPlayer()
except graphics.GraphicsError:
    metrics.writeCSVFile()
    print("Game window was exited.")
except KeyboardInterrupt:
    metrics.writeCSVFile()
    print("Game was halted.")
