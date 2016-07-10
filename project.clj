(defproject drum "0.1.0"
  :description "A sample project that used Clojure for REST API, OAUTH2 and dynamic generated documentation"
  :url "https://gitlab.com/condur/drum"
  :license {:name "Eclipse Public License"
            :url  "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.9.0-alpha9"]]
  :main ^:skip-aot drum.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})
