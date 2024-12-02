from django.utils.safestring import mark_safe

from extras.scripts import Script


class NetBoxTestScript2(Script):
    class Meta:
        name = "Test Script2"
        description = "Print logs for testing purposes."

    def run(self, data, commit):
        self.log_info("Running Test Script")
        self.log_success("This is a success message")
        self.log_success("This is a success message - 2")
        self.log_failure("This is a failure message")
        self.log_warning("This is a warning message")
        self.log_debug("This is a debug message")
        self.log_info("Script completed successfully")
        return mark_safe("Script completed successfully")
