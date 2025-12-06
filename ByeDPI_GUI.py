#!/usr/bin/env python3
"""
ByeDPI Linux GUI
A graphical interface for the ByeDPI application
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
import threading
import os
import signal
import sys


class ByeDPI_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ByeDPI Linux GUI")
        self.root.geometry("800x600")
        
        # Variables for command options
        self.interface_var = tk.StringVar(value="auto")
        self.tcp_mode_var = tk.StringVar(value="desync")
        self.dns_mode_var = tk.StringVar(value="pass")
        self.http_mode_var = tk.StringVar(value="fake")
        self.tls_mode_var = tk.StringVar(value="fake")
        self.port_var = tk.StringVar(value="1080")
        self.bind_addr_var = tk.StringVar(value="127.0.0.1")
        self.md5sig_var = tk.BooleanVar()
        self.transparent_var = tk.BooleanVar()
        self.drop_sack_var = tk.BooleanVar()
        self.tfo_var = tk.BooleanVar()
        self.ipv6_var = tk.BooleanVar()
        self.frag_var = tk.BooleanVar()
        self.frag_off_var = tk.StringVar(value="8")
        self.frag_unit_var = tk.StringVar(value="tcp")
        self.no_sni_var = tk.BooleanVar()
        self.http_host_var = tk.StringVar()
        self.http_ua_var = tk.StringVar()
        self.http_accept_var = tk.StringVar()
        self.http_accept_lang_var = tk.StringVar()
        self.http_accept_enc_var = tk.StringVar()
        self.http_accept_charset_var = tk.StringVar()
        self.http_upgrade_insecure_var = tk.BooleanVar()
        self.http_cookies_var = tk.StringVar()
        self.http_auth_var = tk.StringVar()
        self.http_referer_var = tk.StringVar()
        self.http_origin_var = tk.StringVar()
        self.http_alt_svc_var = tk.StringVar()
        self.http_req_method_var = tk.StringVar(value="GET")
        self.tls_rec_ver_var = tk.StringVar(value="1.2")
        self.tls_cli_ver_var = tk.StringVar(value="1.2")
        self.tls_sni_var = tk.StringVar()
        self.tls_ext_var = tk.BooleanVar()
        self.tls_ciphers_var = tk.StringVar()
        self.tls_groups_var = tk.StringVar()
        self.tls_sig_algs_var = tk.StringVar()
        self.tls_ems_var = tk.BooleanVar()
        self.tls_renego_var = tk.BooleanVar()
        self.tls_tickets_var = tk.BooleanVar()
        self.tls_compress_var = tk.BooleanVar()
        self.tls_psk_var = tk.BooleanVar()
        self.tls_fallback_var = tk.BooleanVar()
        self.tls_cli_ext_var = tk.BooleanVar()
        self.dns_addr_var = tk.StringVar(value="1.1.1.1:53")
        self.dns_fake_addr_var = tk.StringVar(value="1.0.0.1:53")
        self.dns_ttl_var = tk.StringVar(value="600")
        self.dns_sni_var = tk.BooleanVar()
        self.dns_http_var = tk.BooleanVar()
        self.dns_https_var = tk.BooleanVar()
        self.dns_upgrade_var = tk.BooleanVar()
        self.log_level_var = tk.StringVar(value="info")
        self.daemon_var = tk.BooleanVar()
        
        self.process = None
        self.setup_gui()
    
    def setup_gui(self):
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(5, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="ByeDPI Linux GUI", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Basic Options Frame
        basic_frame = ttk.LabelFrame(main_frame, text="Basic Options", padding="10")
        basic_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        basic_frame.columnconfigure(1, weight=1)
        
        # Interface
        ttk.Label(basic_frame, text="Interface:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        interface_entry = ttk.Entry(basic_frame, textvariable=self.interface_var, width=20)
        interface_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 5))
        ttk.Label(basic_frame, text="(auto for automatic detection)").grid(row=0, column=2, sticky=tk.W)
        
        # Port
        ttk.Label(basic_frame, text="Port:").grid(row=1, column=0, sticky=tk.W, padx=(0, 5), pady=(5, 0))
        port_entry = ttk.Entry(basic_frame, textvariable=self.port_var, width=20)
        port_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(0, 5), pady=(5, 0))
        
        # Bind Address
        ttk.Label(basic_frame, text="Bind Address:").grid(row=2, column=0, sticky=tk.W, padx=(0, 5), pady=(5, 0))
        bind_entry = ttk.Entry(basic_frame, textvariable=self.bind_addr_var, width=20)
        bind_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(0, 5), pady=(5, 0))
        
        # Protocol Modes Frame
        modes_frame = ttk.LabelFrame(main_frame, text="Protocol Modes", padding="10")
        modes_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        modes_frame.columnconfigure(1, weight=1)
        
        # TCP Mode
        ttk.Label(modes_frame, text="TCP Mode:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        tcp_mode_combo = ttk.Combobox(modes_frame, textvariable=self.tcp_mode_var, values=["desync", "split", "fake"], width=15)
        tcp_mode_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 5))
        
        # DNS Mode
        ttk.Label(modes_frame, text="DNS Mode:").grid(row=1, column=0, sticky=tk.W, padx=(0, 5), pady=(5, 0))
        dns_mode_combo = ttk.Combobox(modes_frame, textvariable=self.dns_mode_var, values=["pass", "fake", "block"], width=15)
        dns_mode_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(0, 5), pady=(5, 0))
        
        # HTTP Mode
        ttk.Label(modes_frame, text="HTTP Mode:").grid(row=2, column=0, sticky=tk.W, padx=(0, 5), pady=(5, 0))
        http_mode_combo = ttk.Combobox(modes_frame, textvariable=self.http_mode_var, values=["fake", "pass"], width=15)
        http_mode_combo.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(0, 5), pady=(5, 0))
        
        # TLS Mode
        ttk.Label(modes_frame, text="TLS Mode:").grid(row=3, column=0, sticky=tk.W, padx=(0, 5), pady=(5, 0))
        tls_mode_combo = ttk.Combobox(modes_frame, textvariable=self.tls_mode_var, values=["fake", "pass"], width=15)
        tls_mode_combo.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=(0, 5), pady=(5, 0))
        
        # Advanced Options Frame
        advanced_frame = ttk.LabelFrame(main_frame, text="Advanced Options", padding="10")
        advanced_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        advanced_frame.columnconfigure(1, weight=1)
        
        # Checkboxes for various options
        ttk.Checkbutton(advanced_frame, text="MD5 Signature (Linux)", variable=self.md5sig_var).grid(row=0, column=0, sticky=tk.W, padx=(0, 20))
        ttk.Checkbutton(advanced_frame, text="Transparent Proxy (Linux)", variable=self.transparent_var).grid(row=0, column=1, sticky=tk.W)
        ttk.Checkbutton(advanced_frame, text="Drop SACK (Linux)", variable=self.drop_sack_var).grid(row=1, column=0, sticky=tk.W, padx=(0, 20), pady=(5, 0))
        ttk.Checkbutton(advanced_frame, text="TCP Fast Open (Linux)", variable=self.tfo_var).grid(row=1, column=1, sticky=tk.W, pady=(5, 0))
        ttk.Checkbutton(advanced_frame, text="IPv6 Support", variable=self.ipv6_var).grid(row=2, column=0, sticky=tk.W, padx=(0, 20), pady=(5, 0))
        ttk.Checkbutton(advanced_frame, text="Fragment Packets", variable=self.frag_var).grid(row=2, column=1, sticky=tk.W, pady=(5, 0))
        
        # Fragment offset
        ttk.Label(advanced_frame, text="Fragment Offset:").grid(row=3, column=0, sticky=tk.W, padx=(20, 5), pady=(5, 0))
        frag_off_entry = ttk.Entry(advanced_frame, textvariable=self.frag_off_var, width=10)
        frag_off_entry.grid(row=3, column=1, sticky=tk.W, pady=(5, 0))
        
        # Fragment unit
        ttk.Label(advanced_frame, text="Fragment Unit:").grid(row=4, column=0, sticky=tk.W, padx=(20, 5), pady=(5, 0))
        frag_unit_combo = ttk.Combobox(advanced_frame, textvariable=self.frag_unit_var, values=["tcp", "tls", "http"], width=10)
        frag_unit_combo.grid(row=4, column=1, sticky=tk.W, pady=(5, 0))
        
        # HTTP Headers Frame
        http_frame = ttk.LabelFrame(main_frame, text="HTTP Headers", padding="10")
        http_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        http_frame.columnconfigure(1, weight=1)
        
        # Host
        ttk.Label(http_frame, text="Host:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        host_entry = ttk.Entry(http_frame, textvariable=self.http_host_var, width=30)
        host_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 5))
        
        # User Agent
        ttk.Label(http_frame, text="User-Agent:").grid(row=1, column=0, sticky=tk.W, padx=(0, 5), pady=(5, 0))
        ua_entry = ttk.Entry(http_frame, textvariable=self.http_ua_var, width=30)
        ua_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(0, 5), pady=(5, 0))
        
        # Accept
        ttk.Label(http_frame, text="Accept:").grid(row=2, column=0, sticky=tk.W, padx=(0, 5), pady=(5, 0))
        accept_entry = ttk.Entry(http_frame, textvariable=self.http_accept_var, width=30)
        accept_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(0, 5), pady=(5, 0))
        
        # Accept-Language
        ttk.Label(http_frame, text="Accept-Language:").grid(row=3, column=0, sticky=tk.W, padx=(0, 5), pady=(5, 0))
        accept_lang_entry = ttk.Entry(http_frame, textvariable=self.http_accept_lang_var, width=30)
        accept_lang_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=(0, 5), pady=(5, 0))
        
        # Accept-Encoding
        ttk.Label(http_frame, text="Accept-Encoding:").grid(row=4, column=0, sticky=tk.W, padx=(0, 5), pady=(5, 0))
        accept_enc_entry = ttk.Entry(http_frame, textvariable=self.http_accept_enc_var, width=30)
        accept_enc_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), padx=(0, 5), pady=(5, 0))
        
        # Checkboxes for additional HTTP options
        ttk.Checkbutton(http_frame, text="No SNI", variable=self.no_sni_var).grid(row=5, column=0, sticky=tk.W, padx=(0, 20), pady=(5, 0))
        ttk.Checkbutton(http_frame, text="Upgrade Insecure Requests", variable=self.http_upgrade_insecure_var).grid(row=5, column=1, sticky=tk.W, pady=(5, 0))
        
        # Log level
        ttk.Label(main_frame, text="Log Level:").grid(row=5, column=0, sticky=tk.W, pady=(0, 5))
        log_level_combo = ttk.Combobox(main_frame, textvariable=self.log_level_var, values=["error", "warn", "info", "debug"], width=10)
        log_level_combo.grid(row=5, column=1, sticky=tk.W, pady=(0, 5))
        
        ttk.Checkbutton(main_frame, text="Run as Daemon", variable=self.daemon_var).grid(row=6, column=0, columnspan=2, sticky=tk.W, pady=(5, 10))
        
        # Control buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=2, pady=(10, 10))
        
        self.start_button = ttk.Button(button_frame, text="Start ByeDPI", command=self.start_byedpi)
        self.start_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.stop_button = ttk.Button(button_frame, text="Stop ByeDPI", command=self.stop_byedpi, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.generate_button = ttk.Button(button_frame, text="Generate Command", command=self.generate_command)
        self.generate_button.pack(side=tk.LEFT)
        
        # Output text area
        output_label = ttk.Label(main_frame, text="Output:")
        output_label.grid(row=8, column=0, columnspan=2, sticky=tk.W, pady=(10, 0))
        
        self.output_text = scrolledtext.ScrolledText(main_frame, height=10)
        self.output_text.grid(row=9, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(5, 0))
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=10, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
    
    def generate_command(self):
        """Generate the ByeDPI command based on current settings"""
        cmd = ["./ciadpi"]
        
        # Add interface
        if self.interface_var.get():
            cmd.extend(["-i", self.interface_var.get()])
        
        # Add port
        cmd.extend(["-p", self.port_var.get()])
        
        # Add bind address
        cmd.extend(["-b", self.bind_addr_var.get()])
        
        # Add protocol modes
        cmd.extend(["-T", self.tcp_mode_var.get()])
        cmd.extend(["-D", self.dns_mode_var.get()])
        cmd.extend(["-H", self.http_mode_var.get()])
        cmd.extend(["-L", self.tls_mode_var.get()])
        
        # Add advanced options
        if self.md5sig_var.get():
            cmd.append("-S")
        if self.transparent_var.get():
            cmd.append("-E")
        if self.drop_sack_var.get():
            cmd.append("-Y")
        if self.tfo_var.get():
            cmd.append("-F")
        if self.ipv6_var.get():
            cmd.append("-6")
        if self.frag_var.get():
            cmd.extend(["-f", f"{self.frag_off_var.get()},{self.frag_unit_var.get()}"])
        
        # Add HTTP headers
        if self.http_host_var.get():
            cmd.extend(["-h", self.http_host_var.get()])
        if self.http_ua_var.get():
            cmd.extend(["-U", self.http_ua_var.get()])
        if self.http_accept_var.get():
            cmd.extend(["--http-accept", self.http_accept_var.get()])
        if self.http_accept_lang_var.get():
            cmd.extend(["--http-accept-language", self.http_accept_lang_var.get()])
        if self.http_accept_enc_var.get():
            cmd.extend(["--http-accept-encoding", self.http_accept_enc_var.get()])
        if self.http_accept_charset_var.get():
            cmd.extend(["--http-accept-charset", self.http_accept_charset_var.get()])
        if self.http_cookies_var.get():
            cmd.extend(["--http-cookies", self.http_cookies_var.get()])
        if self.http_auth_var.get():
            cmd.extend(["--http-auth", self.http_auth_var.get()])
        if self.http_referer_var.get():
            cmd.extend(["--http-referer", self.http_referer_var.get()])
        if self.http_origin_var.get():
            cmd.extend(["--http-origin", self.http_origin_var.get()])
        if self.http_alt_svc_var.get():
            cmd.extend(["--http-alt-svc", self.http_alt_svc_var.get()])
        
        # Add HTTP options
        if self.no_sni_var.get():
            cmd.append("--no-sni")
        if self.http_upgrade_insecure_var.get():
            cmd.append("--http-upgrade-insecure-requests")
        if self.http_req_method_var.get() != "GET":
            cmd.extend(["--http-req-method", self.http_req_method_var.get()])
        
        # Add TLS options
        if self.tls_rec_ver_var.get() != "1.2":
            cmd.extend(["--tls-rec-ver", self.tls_rec_ver_var.get()])
        if self.tls_cli_ver_var.get() != "1.2":
            cmd.extend(["--tls-cli-ver", self.tls_cli_ver_var.get()])
        if self.tls_sni_var.get():
            cmd.extend(["--tls-sni", self.tls_sni_var.get()])
        if self.tls_ext_var.get():
            cmd.append("--tls-ext")
        if self.tls_ciphers_var.get():
            cmd.extend(["--tls-ciphers", self.tls_ciphers_var.get()])
        if self.tls_groups_var.get():
            cmd.extend(["--tls-groups", self.tls_groups_var.get()])
        if self.tls_sig_algs_var.get():
            cmd.extend(["--tls-sig-algs", self.tls_sig_algs_var.get()])
        if self.tls_ems_var.get():
            cmd.append("--tls-ems")
        if self.tls_renego_var.get():
            cmd.append("--tls-renego")
        if self.tls_tickets_var.get():
            cmd.append("--tls-tickets")
        if self.tls_compress_var.get():
            cmd.append("--tls-compress")
        if self.tls_psk_var.get():
            cmd.append("--tls-psk")
        if self.tls_fallback_var.get():
            cmd.append("--tls-fallback")
        if self.tls_cli_ext_var.get():
            cmd.append("--tls-cli-ext")
        
        # Add DNS options
        if self.dns_addr_var.get() != "1.1.1.1:53":
            cmd.extend(["--dns-addr", self.dns_addr_var.get()])
        if self.dns_fake_addr_var.get() != "1.0.0.1:53":
            cmd.extend(["--dns-fake-addr", self.dns_fake_addr_var.get()])
        if self.dns_ttl_var.get() != "600":
            cmd.extend(["--dns-ttl", self.dns_ttl_var.get()])
        if self.dns_sni_var.get():
            cmd.append("--dns-sni")
        if self.dns_http_var.get():
            cmd.append("--dns-http")
        if self.dns_https_var.get():
            cmd.append("--dns-https")
        if self.dns_upgrade_var.get():
            cmd.append("--dns-upgrade")
        
        # Add log level
        cmd.extend(["-v", self.log_level_var.get()])
        
        # Add daemon option
        if self.daemon_var.get():
            cmd.append("-d")
        
        command_str = " ".join(cmd)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Generated command:\n{command_str}\n\n")
        self.status_var.set("Command generated")
        return cmd
    
    def start_byedpi(self):
        """Start the ByeDPI process"""
        try:
            cmd = self.generate_command()
            self.output_text.insert(tk.END, f"Starting ByeDPI with command:\n{' '.join(cmd)}\n\n")
            
            # Start the process
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                bufsize=1
            )
            
            # Enable stop button, disable start button
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.status_var.set("ByeDPI is running")
            
            # Start reading output in a separate thread
            threading.Thread(target=self.read_output, daemon=True).start()
            
        except FileNotFoundError:
            messagebox.showerror("Error", "ByeDPI executable not found. Make sure 'ciadpi' is in the current directory and compiled.")
            self.status_var.set("Error: ByeDPI executable not found")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start ByeDPI: {str(e)}")
            self.status_var.set(f"Error: {str(e)}")
    
    def stop_byedpi(self):
        """Stop the ByeDPI process"""
        if self.process:
            try:
                # Terminate the process gracefully
                self.process.terminate()
                self.process.wait(timeout=5)  # Wait up to 5 seconds
            except subprocess.TimeoutExpired:
                # Force kill if it doesn't terminate gracefully
                self.process.kill()
            except Exception as e:
                print(f"Error stopping process: {e}")
            
            self.process = None
        
        # Update button states
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.output_text.insert(tk.END, "\nByeDPI stopped.\n")
        self.status_var.set("ByeDPI stopped")
    
    def read_output(self):
        """Read output from the ByeDPI process"""
        if self.process:
            for line in iter(self.process.stdout.readline, ''):
                self.output_text.insert(tk.END, line)
                self.output_text.see(tk.END)  # Auto-scroll to the end
                self.root.update_idletasks()  # Update the GUI
            
            # Process has ended
            self.process.stdout.close()
            self.process = None
            
            # Update GUI
            self.root.after(0, self.on_process_end)
    
    def on_process_end(self):
        """Called when the process ends"""
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_var.set("ByeDPI process ended")


def main():
    root = tk.Tk()
    app = ByeDPI_GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()